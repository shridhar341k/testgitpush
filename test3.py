import pymongo

client = pymongo.MongoClient("mongodb+srv://shridhar341k:shridhar123@cluster0.hvned.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database=client['inventory']
collection=database['table']
data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]
# collection.insert_many(data)
# d=collection.find()
# for i in d:
#     print(i)

#looking for the data where status is 'A'
# d=collection.find({"status":'A'})
# for i in d:
#     print(i)
#looking for the data where status is either 'A' or 'P'
# d=collection.find({"status":{'$in':['A','P']}})
# for i in d:
#     print(i)

#looking for the data where status is greater than C
# d=collection.find({"status":{'$gt':'C'}})
# for i in d:
#     print(i)
#looking for the data where qty is greater than or equal to 100
# d=collection.find({"qty":{'$gte':75}})
# for i in d:
#     print(i)

#looking for the data where qty  equal to 95 and item eual to sketch pad
# d=collection.find({'item':'sketch pad','qty':95})
# for i in d:
#     print(i)
#looking for the data where qty  >=75 and item equal to sketch pad
# d=collection.find({'item':'sketch pad','qty':{'$gte':75}})
# for i in d:
#     print(i)

#looking for the data where qty  >=75 or item equal to sketch pad
# d=collection.find({'$or': [{'item':'sketch pad'},{'qty':{'$gte':75}}]})
# # for i in d:
# #     print(i)

# # whereevr item=canvas update that item=sudhanshu
# collection.update_one({'item':'canvas'}, {'$set' : {'item':'Shridhar'}})
# d=collection.find({'item':'Shridhar'})
# for i in d:
#     print(i)

# for delelting the record
collection.delete_one({'item':'Shridhar'})
d=collection.find({'item':'Shridhar'})
for i in d:
    print(i)