import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('/home/ubuntu/project/ApitoMongo/Insert/HMOData/data/HMO_Data_for_Hillingdon.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client=MongoClient() 
db=mongo_client.test
db.HmoListHillingdon.drop()
header= ["No","Street","Town","County","Postcode","Ward","Floors","Tenants","Lettings","DateLicensed","FeePaid","LTitle","LInitial","LSurname" ]
#fieldnames=header
for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.HmoListHillingdon.insert(row)
