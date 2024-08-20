import pymongo


# this function is used to store the article data into mongo DB
def storeToMongoDB(article_data):
    # connect to mongo DB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["DataEngine"]
    collection = db["Articles"]

    # Load and insert JSON data
    collection.insert_many(article_data)
    print("Data inserted successfully!")
