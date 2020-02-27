import pymongo




class ConexionMongo():

    db_name = "agenda_oscar"
    db_URI = "mongodb://127.0.0.1:27017/"

    def __init__(self):
        # creaos el cliente pasando la direccion ip del servidor de bd y el puerto
        self.client = pymongo.MongoClient(self.db_URI)
        # hacemos referencia a la bd que nos vamos a conectar suponiendo que ya esta creada pasandole como parametro el nombre
        self.mdb = self.client[self.db_name]
    
    def connect_mongo(self):
        return self.mdb
    


