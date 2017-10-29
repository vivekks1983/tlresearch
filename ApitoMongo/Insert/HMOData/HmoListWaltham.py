import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('/home/ubuntu/project/ApitoMongo/Insert/HMOData/data/HMO_Data_for_Waltham.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client=MongoClient() 
db=mongo_client.test
db.HmoListWaltham.drop()
header= ["duration","houseno","street","Location","Postcode","licenceholdername","floors","livingrooms","bedrooms","kitchens","scflats","nonsc","nohouseholds","Permittedoccupants","washhandbasin","baths","showers","wc","dateissued" ]
#fieldnames=header
for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.HmoListWaltham.insert(row)
