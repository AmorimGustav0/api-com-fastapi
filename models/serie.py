from pydantic import BaseModel

class Serie(BaseModel):
    titulo: str
    descricao: str
    ano_lancamento: int


