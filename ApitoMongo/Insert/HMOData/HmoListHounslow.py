import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('/home/ubuntu/project/ApitoMongo/Insert/HMOData/data/HMO_Data_for_Hounslow.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client=MongoClient() 
db=mongo_client.test
db.HmoListHounslow.drop()
header= ["LicenceHolder","AddressofProperty","NumberofHouseholds","NumberofPersons","ExpiryDate"]
#fieldnames=header
for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.HmoListHounslow.insert(row)
