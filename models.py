from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import validator
from datetime import datetime, date



# Modelo para a tabela `Categoria`
class Categoria(SQLModel, table=True):
    cod_categoria: str = Field(primary_key=True)         
    categoria: Optional[str] = None                      
    cod_dre: Optional[int] = None                        

# Modelo para a tabela `DRE`
class DRE(SQLModel, table=True):
    cod_dre: int = Field(primary_key=True)               
    descricao: Optional[str] = None                      
    operacao: Optional[str] = None                       
    tipo: Optional[str] = None                           

# Modelo para a tabela `Lancamentos`
class Lancamentos(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)          
    cod_categoria: Optional[str] = None                  
    grupo: Optional[str] = None                          
    natureza: Optional[str] = None                       
    status: Optional[str] = None                         
    data_pagamento: Optional[str] = None                 
    cod_conta: Optional[int] = None                      
    cod_cliente: Optional[float] = None                  
    valor: Optional[str] = None                        