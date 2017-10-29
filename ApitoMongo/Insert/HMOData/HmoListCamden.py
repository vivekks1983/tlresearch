import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('/home/ubuntu/project/ApitoMongo/Insert/HMOData/data/HMO_Data_for_Camden.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client=MongoClient() 
db=mongo_client.test
db.HmoListCamden.drop()
header= ["PropertyAddress","NameOfLicenceHolder","AddressOfLicenceHolder","MaximumNumberOfPersons","CommencementDate","EndDate","DurationInYears","StoreysOfHMO","NumberOfRooms","NumberOfLivingRooms","NumberOfBedrooms","NumberOfKitchens","NumberOfSelfContainedFlats","NumberOfNonSelfContainedFlats","NumberOfSharedSinks","NumberOfSharedWHBs","NumberOfSharedShowers","NumberOfSharedWCs","NumberOfSharedBaths" ]
#fieldnames=header
for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.HmoListCamden.insert(row)
