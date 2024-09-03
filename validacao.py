import pandas as pd
import pandera as pa

# Definindo schemas para validação dos dados
lancamentos_schema = pa.DataFrameSchema({
    "cod.categoria": pa.Column(pa.String, coerce=True),
    "valor": pa.Column(pa.Float, coerce=True),
    "grupo": pa.Column(pa.String, coerce=True),
    "natureza": pa.Column(pa.String, coerce=True),
    "status": pa.Column(pa.String, coerce=True),
    "data.pagamento": pa.Column(pa.String, coerce=True),  # Ajuste se necessário
})

categorias_schema = pa.DataFrameSchema({
    "cod.dre": pa.Column(pa.String, coerce=True),
    "descricao": pa.Column(pa.String, coerce=True),
    "operacao": pa.Column(pa.String, coerce=True, nullable=True),  # Permitir valores nulos
    "tipo": pa.Column(pa.String, coerce=True),
})

# Função para validar e processar os dados
def validate_and_process_data(lancamentos: pd.DataFrame, categorias: pd.DataFrame):
    # Corrigir separador decimal
    lancamentos['valor'] = lancamentos['valor'].str.replace(',', '.')
    
    # Validar os dados com os schemas definidos
    lancamentos = lancamentos_schema.validate(lancamentos)
    categorias = categorias_schema.validate(categorias)
    
    # Merge dos dados para criar o dataset principal
    data = pd.merge(
        lancamentos,
        categorias,
        left_on='cod.categoria',
        right_on='cod.dre',
        how='left'
    )

    # Converter a coluna de valor para numérico
    data['valor'] = pd.to_numeric(data['valor'], errors='coerce')
    
    return data
