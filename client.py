from pymongo import MongoClient
import json
client = MongoClient("mongodb://%s:%s@127.0.0.1" % ("dap", "dap"))

db=client['DAP_TABA']

collection=db['Water']
'''
import datetime
#this is single sample document to be stored in collection
post={"author":"Mike",
      "text":"My first blog, Plz share and subscribe",
      "tags": ["mongodb","python","pymongo"],
      "date": datetime.datetime.utcnow()
      }

posts=db.posts
post_id=posts.insert_one(post).inserted_id
print(post_id)

print(db.list_collection_names())
'''


with open("Water_Consumption.json") as f:
    data=json.load(f)

collection.insert_many(data)


    