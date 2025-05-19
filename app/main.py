from fastapi import FastAPI
from routes.series import create_item, delete_item, update_item, read_item, Ator_serie
from models.database import Database

app = FastAPI()

@app.get('/') # define a rota raiz
def read_root():
    return {"Series": "Must Watch"}

@app.get("/{table_name}/{item_id}")
def get_routes(table_name: str, item_id: int = None):
    return read_item(table_name, item_id)

@app.post("/{table_name}")
def create_routes(table_name: str, item: dict):
    return create_item(table_name, item)

@app.put("/{table_name}/{item_id}")
def update_routes(table_name: str, item_id: int, item: dict):
    return update_item(table_name, item_id, item)

@app.delete("/{table_name}/{item_id}")
def delete_routes(table_name: str, item_id: int):
    return delete_item(table_name, item_id)

@app.post("/ator_serie/completo")
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




