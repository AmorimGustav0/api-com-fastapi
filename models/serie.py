from fastapi import HTTPException
from models.database import Database, tables
from pydantic import BaseModel


""" db = Database() """
tb = tables()







def get_nome_coluna(table_name: str):
    return {
        "serie": "titulo",
        "categoria": "nome_categoria",
        "ator": "nome",
        "ator_serie": "personagem"
    }.get(table_name)


def get_id_by_name(table_name: str, nome: str):
    
    coluna = get_nome_coluna(table_name)
    if not coluna:
        raise HTTPException(status_code=400, detail="Tabela não permitida")
    
    with Database() as db:

        query = f"SELECT {tb.PRIMARY_KEYS[table_name]} FROM {table_name} WHERE {coluna} LIKE %s LIMIT 1"
        resultado = db.consultar(query, (f"%{nome}%",))

        if not resultado:
            raise HTTPException(status_code=404, detail="Item não encontrado")

        return resultado[0][tb.PRIMARY_KEYS[table_name]]



class TabelaService:

    @staticmethod
    def gettotal(table_name: str, item_id: int = None):
        coluna_id = tb.PRIMARY_KEYS.get(table_name)
        if not coluna_id:
            raise HTTPException(status_code=400, detail="Tabela não permitida")

        try:
            with Database() as db:
                if item_id is None:
                    sql = f"SELECT * FROM {table_name}"
                    params = ()
                else:
                    sql = f"SELECT * FROM {table_name} WHERE {coluna_id} = %s"
                    params = (item_id,)

                resultado = db.consultar(sql, params)

                if not resultado:
                    raise HTTPException(status_code=404, detail="Item não encontrado")

                return resultado

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao consultar o banco de dados: {str(e)}")
 
    @staticmethod
    def read_item(table_name: str, nome: str):
        try:
            id_valor = get_id_by_name(table_name, nome)
            coluna_id = tb.PRIMARY_KEYS[table_name]

            with Database() as db:
                sql = f"SELECT * FROM {table_name} WHERE {coluna_id} = %s"
                resultado = db.consultar(sql, (id_valor,))

                if not resultado:
                    raise HTTPException(status_code=404, detail="Item não encontrado")

                return resultado

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao consultar o banco de dados: {str(e)}")

    @staticmethod
    def create_item(table_name: str, item: dict):
        if table_name not in tb.TABELAS:
            raise HTTPException(status_code=400, detail="Tabela não permitida")

        columns = tb.TABELAS[table_name]
        colunas = ', '.join(columns)
        marcador = ', '.join(['%s'] * len(columns))

        # Caso especial para avaliacao_serie com NOW()
        if table_name == 'avaliacao_serie':
            colunas += ', data_avaliacao'
            marcador += ', NOW()'

        sql = f"INSERT INTO {table_name} ({colunas}) VALUES ({marcador})"
        params = tuple(item[col] for col in columns)

        try:
            with Database() as db:
                db.executar(sql, params)
            return {"message": "Item adicionado com sucesso!"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao adicionar o item: {str(e)}")

    @staticmethod
    def update_item(table_name: str, nome: str, item: dict):
        if table_name not in tb.TABELAS:
            raise HTTPException(status_code=400, detail="Tabela não permitida")

        try:
            id_valor = get_id_by_name(table_name, nome)
            colunas = tb.TABELAS[table_name]
            chave_primaria = tb.PRIMARY_KEYS[table_name]

            set_clause = ', '.join([f"{col} = %s" for col in colunas])
            sql = f"UPDATE {table_name} SET {set_clause} WHERE {chave_primaria} = %s"
            params = tuple(item[col] for col in colunas) + (id_valor,)

            with Database() as db:
                db.executar(sql, params)

            return {"message": "Item atualizado com sucesso!"}

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao atualizar o item: {str(e)}")

    @staticmethod
    def delete_item(table_name: str, nome: str):
        if table_name not in tb.PRIMARY_KEYS:
            raise HTTPException(status_code=400, detail="Tabela não permitida")

        try:
            id_valor = get_id_by_name(table_name, nome)
            chave_primaria = tb.PRIMARY_KEYS[table_name]
            sql = f"DELETE FROM {table_name} WHERE {chave_primaria} = %s"

            with Database() as db:
                db.executar(sql, (id_valor,))

            return {"message": "Item removido com sucesso!"}

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao remover o item: {str(e)}")



class Ator_serie(BaseModel):
    nome_ator: str
    titulo: str
    personagem: str