from project import app
from pymongo import MongoClient

client = MongoClient(app.config['MONGO_URI'])

db = client[app.config['MONGO_DBNAME']]
collection = db.images_collection
