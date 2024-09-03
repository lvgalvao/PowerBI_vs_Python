from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do .env
load_dotenv()

# Função para conectar ao banco de dados
def connect_to_db():
    username = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    dbname = os.getenv('DB_NAME')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')

    # String de conexão com o banco de dados
    engine = create_engine(
        f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}'
    )
    return engine

# Função para obter dados das tabelas
def get_table_data(engine, query):
    with engine.connect() as connection:
        data = pd.read_sql(query, connection)
    return data

# Coleta de dados das tabelas
def fetch_data():
    engine = connect_to_db()
    query_lancamentos = """
        SELECT *
        FROM lancamentos
    """
    query_categorias = """
        SELECT *
        FROM categorias
    """
    lancamentos = get_table_data(engine, query_lancamentos)
    categorias = get_table_data(engine, query_categorias)
    return lancamentos, categorias
