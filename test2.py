import pymongo

client = pymongo.MongoClient("mongodb+srv://shridhar341k:shridhar123@cluster0.hvned.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database=client['myinfo']
collection=database["sudh"]
#collection1=database["dpkt"]
# record = collection.find()
# for i in record:
#     print(i)


# data=collection.find({"companyName":"iNeuron"})
data1=collection.find({"courseOffered":{"$gt":"E"}})
for i in data1:
    print(i)
