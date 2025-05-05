from pydantic import BaseModel

class Serie(BaseModel):
    id: str
    titulo: str
    descricao: str
    ano_lancamento: int
    id_categoria: int


