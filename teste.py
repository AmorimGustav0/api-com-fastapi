from models.database import Database

db = Database()
db.conectar()


table_name = "serie"
nome = "homem aranha"

def teste():
    if table_name == "serie":
        resultado = "titulo"
    elif table_name == "categoria":
        resultado = "nome_categoria"
    elif table_name == "ator":
        resultado = "nome"
    else:
        resultado = None
    return resultado

coluna = teste()




query = f"SELECT {db.PRIMARY_KEYS[table_name]} FROM {table_name} WHERE {coluna} LIKE '%{nome}%' LIMIT 1"
resultado = db.select(query)
id_valor = resultado[0][db.PRIMARY_KEYS[table_name]]  # mais genérico
print(f"ID encontrado: {id_valor}")
db.desconectar()



