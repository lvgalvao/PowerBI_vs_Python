import pandas as pd

# Funções para calcular os indicadores
def calculate_indicators(data: pd.DataFrame):
    receita = data[data['operacao'] == 'Receita']['valor'].sum()
    despesa = data[data['operacao'] == 'Despesa']['valor'].sum()
    lucro_bruto = receita - despesa
    receita_por_grupo = data.groupby('grupo')['valor'].sum().reset_index()
    despesas_por_tipo = data[data['operacao'] == 'Despesa'].groupby('tipo')['valor'].sum().reset_index()
    lucro_liquido = receita - despesa  # Ajuste conforme as despesas e deduções específicas

    return receita, despesa, lucro_bruto, receita_por_grupo, despesas_por_tipo, lucro_liquido
