import pymongo

client = pymongo.MongoClient("mongodb+srv://shridhar341k:shridhar123@cluster0.hvned.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)