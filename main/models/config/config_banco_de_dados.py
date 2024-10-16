import os
import time
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

NOME = "      Eliel Academy"

# Criando o banco de dados.
db = create_engine("sqlite:///meubanco.db")

# Conexão com o banco de dados.
Session = sessionmaker(bind=db)
session = Session()

# Criando tabela.
Base = declarative_base()

class Usuario(Base):
    # Definindo nome da tabela.
    __tablename__ = "usuarios"

    # Definindo atributos da tabela.
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # Definindo atributos da classe.
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)