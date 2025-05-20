from fastapi import HTTPException
from models.database import Database
from pydantic import BaseModel

 
db = Database()
series_db = []


class funcs():
 
    def read_item(table_name: str, item_id: int = None):
        """
        Consulta uma tabela específica no banco de dados pelo ID.
        """
        db.conectar()  # Conecta ao banco de dados
    
        tabelas_permitidas = {
        'serie': 'id_serie',
        'categoria': 'id_categoria',
        'ator': 'id_ator',
        'motivo_assistir': 'id_motivo',
    }

    
        coluna_id = tabelas_permitidas.get(table_name)
    
        try:
            if item_id is None:
                sql = f"SELECT * FROM {table_name}"
                params = ()
            else:
                sql = f"SELECT * FROM {table_name} WHERE {coluna_id} = %s"
                params = (item_id,)
    
            resultado = db.consultar(sql, params)
            db.desconectar()
        
            if not resultado:
                raise HTTPException(status_code=404, detail="Item não encontrado")
    
            return resultado
        except Exception as e:
            db.desconectar()
            raise HTTPException(status_code=500, detail=f"Erro ao consultar o banco de dados: {str(e)}")


    

    def create_item(table_name: str, item: dict):
        '''Adiciona um item a uma tabela específica no banco de dados'''
        db.conectar()

        try:
            if table_name not in db.TABELAS:
                raise HTTPException(status_code=400, detail="Tabela não permitida")

            columns = db.TABELAS[table_name]
            colunas = ', '.join(columns)
            marcador = ', '.join(['%s'] * len(columns))

            # Caso especial para avaliacao_serie com NOW()
            if table_name == 'avaliacao_serie':
                colunas += ', data_avaliacao'
                marcador += ', NOW()'

            sql = f"INSERT INTO {table_name} ({colunas}) VALUES ({marcador})"
            params = tuple(item[colunas] for colunas in columns)

            db.executar(sql, params)
            db.desconectar()

            return {"message": "Item adicionado com sucesso!"}

        except Exception as e:
            db.desconectar()
            raise HTTPException(status_code=500, detail=f"Erro ao adicionar o item: {str(e)}")
    
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
        

    class Ator_serie(BaseModel):

        nome_ator: str
        titulo: str
        personagem: str 




