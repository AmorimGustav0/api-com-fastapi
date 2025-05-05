from fastapi import APIRouter
from models.database import Database
from models.serie import Serie
 
router = APIRouter(prefix="/series")  # <- isso é importante
db = Database()
series_db = []
 
@router.get("/")

def listar_series():
    
    db.conectar()
    series = db.consultar("SELECT * FROM serie")
    db.desconectar()
    return series  

 
@router.post("/")
def cadastrar(serie: Serie):
    db.conectar()
    sql = "INSERT INTO serie (titulo, descricao, ano_lancamento, id_categoria) VALUES (%s, %s,%s,%s)"
    db.executar(sql,(serie.titulo, serie.descricao,serie.ano_lancamento, serie.id_categoria))
    db.desconectar()
    return {"mensagem": "Série cadastrada com sucesso", "serie": serie}
 