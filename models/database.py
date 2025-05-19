from ast import Dict
from dotenv import load_dotenv
import mysql.connector as mc # Importando a biblioteca do conector do MySQL
from mysql.connector import Error, MySQLConnection# Importando a classe Error para tratar as mensagens de erro do código
from os import getenv
from typing import Optional, Any, Tuple, List, Union


class Database:
    def __init__(self):
        load_dotenv()
        self.host: str = getenv('DB_HOST')
        self.username: str = getenv('DB_USER')
        self.password: str = getenv('DB_PSWD')
        self.database: str = getenv('DB_NAME')
        self.connection: Optional[MySQLConnection] = None # Inicialização da conexão
        self.cursor: Union[List[Dict], None] = None # Inicialização do cursor
 
    def conectar(self)-> None:
        """Estabelece uma conexão com o banco de dados."""
        try:
            self.connection = mc.connect(
                host = self.host,
                database = self.database,
                user = self.username,
                password = self.password
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                print('Conexão ao banco de dados realizada com sucesso!')
        except Error as e:
            print(f'Erro de conexão: {e}')
            self.connection = None
            self.cursor = None
 
    def desconectar(self) -> None:
        """Encerra a conexão com o banco de dados e o cursor, se existirem."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print('Conexão com o banco de dados encerrada com sucesso!')
        
 
    def executar(self, sql: str, params: Optional[Tuple[Any,...]] = None) -> Optional[List[Dict]]:
        """Executa uma instrução no banco de dados."""
        if self.connection is None and self.cursor is None:
            print('Conexão ao banco de dados não estabelecida!')
            return None
        try:
            self.cursor.execute(sql, params)
            self.connection.commit()
            return self.cursor
        except Error as e:
            print(f'Erro de execução: {e}')
            return None
        
    def consultar(self, sql: str, params: Optional[Tuple[Any,...]]= None) -> Optional[List[dict]]: 
        """Executa uma consulta no banco de dados."""
        if self.connection is None and self.cursor is None:
            print('Conexão ao banco de dados não estabelecida!')
            return None
        try:
            self.cursor.execute(sql, params)
            # self.connection.commit() -> select não usa commit
            return self.cursor.fetchall()
        except Error as e:
            print(f'Erro de execução: {e}')

            return None
        

    def select(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            print(f'erro: {e}')
            return None
        
    
    
    TABELAS = {
        'serie': ['titulo', 'descricao', 'ano_lancamento', 'id_categoria'],
        'categoria': ['categoria_nome'],
        'ator': ['nome'],
        'motivo_assistir': ['id_serie', 'motivo'],
        'avaliacao_serie': ['id_serie', 'nota', 'comentario']
    }
    
    PRIMARY_KEYS = {
        'serie': 'id_serie',
        'categoria': 'id_categoria',
        'ator': 'id_ator',
        'motivo_assistir': 'id_motivo',
        'avaliacao_serie': 'id_avaliacao'
    }
