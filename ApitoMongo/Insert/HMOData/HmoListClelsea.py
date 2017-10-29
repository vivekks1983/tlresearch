import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('/home/ubuntu/project/ApitoMongo/Insert/HMOData/data/RBKC_Register_of_HMO_Licences_Chelsea.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client=MongoClient() 
db=mongo_client.test
db.HmoListChelsea.drop()
header= ["ReferenceNumber","UPRN","Name","Company","Address","SW5","Address","HBFflats","standard","Tenure","NotReferred","NA","Bedroom","Comments","BedisitsFlats","WCShowers","Number"]
#fieldnames=header
for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.HmoListClelsea.insert(row)
