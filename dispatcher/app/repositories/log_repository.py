from app.db.connection import mongo_connection
from datetime import datetime


class LogRepository:
    def __init__(self):
        self.db = mongo_connection.get_database()
        self.collection = self.db["logs"]

    def add_log(self, method: str, path: str, status_code: int):
        log = {
            "method": method,
            "path": path,
            "status_code": status_code,
            "timestamp": datetime.utcnow()
        }
        self.collection.insert_one(log)

    def get_logs(self):
        logs = list(self.collection.find({}, {"_id": 0}))
        return logs