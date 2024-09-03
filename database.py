from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Conectar ao banco de dados usando as variáveis de ambiente
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Construir a URL de conexão com o banco de dados
DATABASE_URL = f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL, echo=False)

# Criar tabelas no banco de dados
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Função para obter uma sessão de conexão
def get_session():
    return Session(engine)
