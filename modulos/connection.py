from pymongo import MongoClient as pyM
from modulos.segredos import MONGO_CLIENTE

cliente = pyM.MongoClient(MONGO_CLIENTE)

db = cliente.test

tweets_collection = db.tweets