from typing import Optional


class MongoConnection:
    def __init__(self):
        self.client: Optional[object] = None
        self.database: Optional[object] = None

    def connect(self):
        self.client = None
        self.database = None

    def get_database(self):
        return self.database


mongo_connection = MongoConnection()