from models.database import Database

db = Database()

db.conectar()

query = f"Select id_serie from serie where (titulo like '%homem aranha%') limit 1"
id_serie = db.select(query) #retorna uma lista de tuplas
id_serie = id_serie[0]['id_serie']
print(id_serie) 
db.desconectar()