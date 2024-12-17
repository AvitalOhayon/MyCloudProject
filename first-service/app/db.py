from pymongo import MongoClient
from app.config import Config


class Database:
    def __init__(self, uri):
        self.client = MongoClient(uri)
        self.db = self.client['users_db']

    def get_collection(self, collection_name):
        return self.db[collection_name]


db = Database(Config.MONGO_URI)
