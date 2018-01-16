import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('/home/ubuntu/project/ApitoMongo/Insert/HMOData/data/HMODataFOI.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client=MongoClient() 
db=mongo_client.test
db.HMODataFOI.drop()
header= ["Council","Licensed","Unlicensed2016","Unlicensed2015","D","E","F","G","H","I" ]
#fieldnames=header
for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.HMODataFOI.insert(row)
