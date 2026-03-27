from pymongo import MongoClient


class MongoConnection:
    def __init__(self):
        try:
            self.client = MongoClient("mongodb://localhost:27017")
            self.database = self.client["user_db"]
            print("MongoDB bağlantısı başarılı (user_db)")
        except Exception as e:
            print("MongoDB bağlantı hatası:", e)
            self.client = None
            self.database = None

    def get_database(self):
        if self.database is None:
            raise Exception("MongoDB bağlantısı yok")
        return self.database


mongo_connection = MongoConnection()