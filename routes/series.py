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
    series_db.append(serie)
    return {"mensagem": "Série cadastrada com sucesso", "serie": serie}
 