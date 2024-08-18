import pymongo

# connect to mongo DB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["DataEngine"]
collection = db["Articles"]
