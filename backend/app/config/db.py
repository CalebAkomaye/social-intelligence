from pymongo import MongoClient
from pymongo.server_api import ServerApi
from config.config import URI

client = MongoClient(URI, server_api=ServerApi('1'))
db = client.insight_db

User = db["user"]
