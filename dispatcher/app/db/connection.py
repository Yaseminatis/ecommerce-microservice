import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


class MongoConnection:
    def __init__(self):
        try:
            mongo_uri = os.getenv("MONGO_URI")
            database_name = os.getenv("DATABASE_NAME")

            self.client = MongoClient(mongo_uri)
            self.database = self.client[database_name]

            print(f"Dispatcher MongoDB bağlantısı başarılı ({database_name})")

        except Exception as e:
            print("Dispatcher MongoDB bağlantı hatası:", e)
            self.client = None
            self.database = None

    def get_database(self):
        if self.database is None:
            raise Exception("MongoDB bağlantısı yok")
        return self.database


mongo_connection = MongoConnection()