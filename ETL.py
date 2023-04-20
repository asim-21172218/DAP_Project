import pymongo
from sqlalchemy import create_engine
import pandas as pd

def readFromMongo():
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    database=client["DAP"]
    collection=database["newyork_weather"]
    rowlist=[]
    for document in collection.find():
        rowlist.append(document)
    return rowlist


"""
def loadtopostgre(df,tbl):
    try:
        rows_imported=0
        uid="password"
        pwd="password"
        server="127.0.0.1"
        engine=create_engine(f'postgresql://{uid}:{pwd}@{server}:5432/DAP_Project')

"""
if __name__=="__main__":
    
    data=readFromMongo()
    print(len(data))