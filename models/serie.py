from pydantic import BaseModel
from models.database import Database

db = Database
class Ator_serie(BaseModel):

    nome_ator: str
    titulo: str
    personagem: str 

class Serie(BaseModel):
    titulo: str
    descricao: str
    ano_lancamento: int
    id_categoria: int

class Ator(BaseModel):
    nome: str
    ano_nasc: int





   

