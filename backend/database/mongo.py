from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_DATABASE_URL = os.getenv("MONGO_DATABASE_URL")
client = MongoClient(MONGO_DATABASE_URL)
mongo_db = client["shop"]
mongo_products = mongo_db["products"]
