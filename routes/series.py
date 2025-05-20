from fastapi import APIRouter, FastAPI
from models.serie import TabelaService, Ator_serie
from models.database import Database

f = TabelaService()
router = APIRouter()
app = FastAPI()



@router.get('/') # define a rota raiz
def read_root():
    return {"Series": "Must Watch"}


@router.get('/{table_name}')
def get_total_routes(table_name: str, item_id: int = None):
    return f.gettotal(table_name, item_id)

@router.get("/{table_name}/{nome}")
def get_routes(table_name: str, nome: str = None):
    return f.read_item(table_name, nome)

@router.post("/{table_name}")
def create_routes(table_name: str, item: dict):
    return f.create_item(table_name, item)

@router.put("/{table_name}/{nome}")
def update_routes(table_name: str, nome: str, item: dict):
    return f.update_item(table_name, nome, item)

@router.delete("/{table_name}/{nome}")
def delete_routes(table_name: str, nome: str):
    return f.delete_item(table_name, nome)

@router.post("/ator_serie/completo")
def criar_ator_serie(ator : Ator_serie):

    db = Database()
    db.conectar()

    query = f"Select id_autor from ator where (nome like '%{ator.nome_ator}%') limit 1"
    id_ator = db.select(query) #retorna uma lista de tuplas
    id_ator = id_ator[0]['id_autor']

    query = f"Select id_serie from serie where (titulo like '%{ator.titulo}%') limit 1"
    id_serie = db.select(query) #retorna uma lista de tuplas
    id_serie = id_serie[0]['id_serie']



    sql = "INSERT INTO ator_serie (id_serie, id_ator, personagem) VALUES (%s, %s,%s)"
    db.executar(sql,(id_serie,id_ator, ator.personagem))
    db.desconectar()
    return {"mensagem": "Série vinculada ao ator com sucesso"}




