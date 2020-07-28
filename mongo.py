import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myBookRoom"
COLLECTION_NAME = "bookRoom"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.CobbectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

new_docs = [{}]

documents = coll.find({'authors': 'J.K. Rowling/Mary GrandPre'})

for doc in documents:
    print(doc)

