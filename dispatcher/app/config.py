import os

AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://127.0.0.1:8001")
USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://127.0.0.1:8002")
PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://127.0.0.1:8003")

