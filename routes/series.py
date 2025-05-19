from fastapi import APIRouter
from fastapi import HTTPException
from models.database import Database
from models.serie import Serie, Ator, Ator_serie
 
router = APIRouter(prefix="/series")  # <- isso é importante
db = Database()
series_db = []
 
@router.get("/")
def listar_series():
    
    db.conectar()
    series = db.consultar("SELECT * FROM serie")
    db.desconectar()
    return series  

@router.get("/ator")
def listar_ator_series():
    
    db.conectar()
    series = db.consultar("SELECT * FROM must_watch.ator_series")
    db.desconectar()
    return series  

 
@router.post("/")
def cadastrar_serie(serie: Serie):
    db.conectar()
    sql = "INSERT INTO serie (titulo, descricao, ano_lancamento, id_categoria) VALUES (%s, %s,%s,%s)"
    db.executar(sql,(serie.titulo, serie.descricao,serie.ano_lancamento, serie.id_categoria))
    db.desconectar()
    return {"mensagem": "Série cadastrada com sucesso", "serie": serie}


@router.post("/ator")
def cadastrar_ator(ator: Ator):
    db.conectar()
    sql = "INSERT INTO ator (nome, ano_nasc) VALUES (%s, %s)"
    db.executar(sql,(ator.nome, ator.ano_nasc))
    db.desconectar()
    return {"mensagem": "Ator cadastrado com sucesso", "ator": ator}

@router.put("/") 
def update_item(table_name: str, item_id: int, item: dict):
    db.conectar()

    try:
        if table_name not in db.TABELAS:
            raise HTTPException(status_code=400, detail="Tabela não permitida")

        colunas = db.TABELAS[table_name]
        chave_primaria = db.PRIMARY_KEYS[table_name]

        set_clause = ', '.join([f"{col} = %s" for col in colunas])
        sql = f"UPDATE {table_name} SET {set_clause} WHERE {chave_primaria} = %s"

        params = tuple(item[col] for col in colunas) + (item_id,)

        db.executar(sql, params)
        db.desconectar()

        return {"message": "Item atualizado com sucesso!"}
    except Exception as e:
        db.desconectar()
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar o item: {str(e)}")
    
@router.delete("/")   
def delete_item(table_name: str, item_id: int):
    '''Remove um item de uma tabela específica no banco de dados'''
    db.conectar()

    try:
        if table_name not in db.PRIMARY_KEYS:
            raise HTTPException(status_code=400, detail="Tabela não permitida")

        chave_primaria = db.PRIMARY_KEYS[table_name]
        sql = f"DELETE FROM {table_name} WHERE {chave_primaria} = %s"

        db.executar(sql, (item_id,))
        db.desconectar()

        return {"message": "Item removido com sucesso!"}

    except Exception as e:
        db.desconectar()
        raise HTTPException(status_code=500, detail=f"Erro ao remover o item: {str(e)}")

@router.post("/ator_serie")
def criar_ator_serie(ator : Ator_serie):
    
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
    


    
