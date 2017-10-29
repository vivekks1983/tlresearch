import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('/home/ubuntu/project/ApitoMongo/Insert/HMOData/data/HMO_Data_for_Barnet.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client=MongoClient() 
db=mongo_client.test
db.HmoListBarnet.drop()
header= ["LicenceeName1","LicenceeName2","LicenceeAddress1","LicenceeAddress2","LicenceeAddress3","LicenseePostcode","LICENSEDPROPERTY","LicenceStartDate","LicenceExpiryDate","Rooms","PermittedNumberofOccupants","LicenceType" ]
#fieldnames=header
for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.HmoListBarnet.insert(row)
