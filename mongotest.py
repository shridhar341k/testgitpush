import pymongo

client = pymongo.MongoClient("mongodb+srv://shridhar341k:shridhar123@cluster0.hvned.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d={
    "name":"sudhanshu",
    "email":"sudhanshi@ineuron.ai",
    "surname":"kumar"
}
d={
    "name":"Shridhar",
    "email":"shridhar341k@gmail.com",
    "surname":"Raghu"
}

db1 = client['mongotest']
coll=db1['test']
coll.insert_one(d)

