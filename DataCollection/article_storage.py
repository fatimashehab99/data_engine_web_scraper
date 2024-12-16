import pymongo
from dataclasses import asdict

# Create a global variable for the client, db, and collection
client = None
db = None
collection = None


def get_db_connection():
    global client, db, collection

    if client is None:
        client = pymongo.MongoClient("mongodb://localhost:27017/")  # Create client if not exists
        db = client["DataEngine"]  # Set db if not exists
        collection = db["Articles"]  # Set collection if not exists

    return collection


# This function stores the article data into MongoDB
def storeToMongoDB(article):
    collection = get_db_connection()  # Get the collection from the reused connection
    article_data = asdict(article)  # Convert dataclass to dictionary
    collection.insert_one(article_data)  # Insert into MongoDB
    print("Data inserted successfully!")
