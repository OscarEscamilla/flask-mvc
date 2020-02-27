import pymongo

# creaos el cliente pasando la direccion ip del servidor de bd y el puerto
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

# hacemos referencia a la bd que nos vamos a conectar suponiendo que ya esta creada pasandole como parametro el nombre
mdb = client["agenda_oscar"]