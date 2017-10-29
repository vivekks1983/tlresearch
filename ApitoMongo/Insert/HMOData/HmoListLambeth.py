import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('/home/ubuntu/project/ApitoMongo/Insert/HMOData/data/HMO_Data_for_Lambeth.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client=MongoClient() 
db=mongo_client.test
db.HmoListLambeth.drop()
header= ["Start_date","NameofLicenceholder","PropertyAddress","Postcode","Category","NumberofStoreys","NumberofRooms","MaxNumberofPersons","Actualnumber","MaxNumberofHouseholds","FormDate","LicenceExpiryDate","Durationoflicence","ScheduleofDeficiencies","ConditionsAttachedtoProperty" ]
#fieldnames=header
for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.HmoListLambeth.insert(row)
