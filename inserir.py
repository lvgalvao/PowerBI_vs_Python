import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Função para conectar ao banco de dados PostgreSQL
def connect_to_db():
    # Carregando variáveis de ambiente
    username = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    dbname = os.getenv('DB_NAME')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')

    # Criando a string de conexão
    engine = create_engine(
        f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}'
    )
    return engine

# Função para carregar o CSV e inserir os dados no banco de dados
def upload_csv_to_postgres(engine, csv_path, table_name):
    try:
        # Lendo o CSV com o delimitador correto
        df = pd.read_csv(csv_path, delimiter=',')  # Delimitador ajustado para vírgula
        # Inserindo os dados na tabela do banco de dados
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Dados inseridos na tabela {table_name} com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")

# Definindo o caminho do CSV e o nome da tabela no banco de dados
csv_path = 'data/dre.csv'  # Substitua pelo caminho correto do seu arquivo CSV
table_name = 'dre'  # Nome desejado para a tabela no banco de dados

# Conectando ao banco de dados e executando o upload
engine = connect_to_db()
upload_csv_to_postgres(engine, csv_path, table_name)
