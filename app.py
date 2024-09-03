import streamlit as st
from conexao import fetch_data
from validacao import validate_and_process_data
from indicadores import calculate_indicators

# Coletar dados das tabelas
lancamentos, categorias = fetch_data()

# Validar e processar os dados
data = validate_and_process_data(lancamentos, categorias)

# Calcular os indicadores
receita, despesa, lucro_bruto, receita_por_grupo, despesas_por_tipo, lucro_liquido = calculate_indicators(data)

# Dashboard no Streamlit
st.title("Dashboard DRE")

# Indicadores principais
st.header("Indicadores Principais")

col1, col2, col3 = st.columns(3)
col1.metric("Receita Total", f"R$ {receita:,.2f}")
col2.metric("Despesa Total", f"R$ {despesa:,.2f}")
col3.metric("Lucro Bruto", f"R$ {lucro_bruto:,.2f}")

# Detalhamento de receitas e despesas
st.subheader("Receitas por Grupo")
st.write(receita_por_grupo)

st.subheader("Despesas por Tipo")
st.write(despesas_por_tipo)

# Lucro Líquido
st.subheader("Lucro Líquido")
st.metric("Lucro Líquido", f"R$ {lucro_liquido:,.2f}")

# Gráfico de barras de Receitas por Grupo
st.bar_chart(receita_por_grupo.set_index('grupo')['valor'])

# Gráfico de barras de Despesas por Tipo
st.bar_chart(despesas_por_tipo.set_index('tipo')['valor'])
