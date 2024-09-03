import pandas as pd
import streamlit as st
from sqlmodel import select
from database import create_db_and_tables, get_session
from models import Lancamentos, Categoria, DRE

# Inicializar o banco de dados e tabelas
create_db_and_tables()

# Função para buscar e processar dados
def fetch_data():
    with get_session() as session:
        # Consultar todos os dados de cada tabela
        lancamentos = session.exec(select(Lancamentos)).all()
        categorias = session.exec(select(Categoria)).all()
        dre = session.exec(select(DRE)).all()

        # Convertendo os resultados para DataFrames
        lancamentos_df = pd.DataFrame([l.model_dump() for l in lancamentos])
        categorias_df = pd.DataFrame([c.model_dump() for c in categorias])
        dre_df = pd.DataFrame([d.model_dump() for d in dre])

        # Retornar os DataFrames ajustados
        return lancamentos_df, categorias_df, dre_df

# Coletar e processar dados
lancamentos_df, categorias_df, dre_df = fetch_data()

# Realizar o `join` entre `lancamentos` e `categoria` com base na `cod_categoria`
merged_df = pd.merge(lancamentos_df, categorias_df, left_on="cod_categoria", right_on="cod_categoria", how="left")

# Realizar o `join` entre o resultado anterior e `dre` com base na `cod_dre`
final_df = pd.merge(merged_df, dre_df, left_on="cod_dre", right_on="cod_dre", how="left")

# Converter a coluna 'valor' para float, substituindo vírgulas por pontos
final_df["valor"] = final_df["valor"].str.replace(',', '.').astype(float)

# Exibir o DataFrame resultante
st.title("Dados Combinados para Cálculo de DRE")
st.write(final_df)

# Calcular Indicadores de Receita, Despesa, Lucro, etc.
# Filtrar valores de receita e despesa conforme a operação definida no DRE
receita = final_df[final_df["operacao"] == "( + )"]["valor"].sum()
despesa = final_df[final_df["operacao"] == "( - )"]["valor"].sum()
lucro_bruto = receita - despesa

# Exibir indicadores no dashboard
st.header("Indicadores de DRE")
st.metric("Receita Total", f"R$ {receita:,.2f}")
st.metric("Despesa Total", f"R$ {despesa:,.2f}")
st.metric("Lucro Bruto", f"R$ {lucro_bruto:,.2f}")
