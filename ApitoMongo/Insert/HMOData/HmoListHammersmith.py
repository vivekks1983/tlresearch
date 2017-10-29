import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('/home/ubuntu/project/ApitoMongo/Insert/HMOData/data/HMO_Data_for_Hammersmith.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client=MongoClient() 
db=mongo_client.test
db.HmoListHammersmith.drop()
header= ["Postcode","Nooffloors","Permittednoofpersons","Dateofissue","Dateofexpiry","AddressofHMOlicensedproperty","Nameoflicenseholder"]
#fieldnames=header
for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.HmoListHammersmith.insert(row)
