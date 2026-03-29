import os
from dotenv import load_dotenv

load_dotenv()

ROUTE_MAP = {
    "login": os.getenv("AUTH_SERVICE_URL"),
    "users": os.getenv("USER_SERVICE_URL"),
    "products": os.getenv("PRODUCT_SERVICE_URL"),
}