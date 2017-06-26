import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('/home/ubuntu/project/ApiToMongo/Insert/LG/data/EducationEmployeeExpenditure.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client=MongoClient() 
db=mongo_client.test
db.EducationEmployeeExpenditure.drop()
header= ["Period_identifier","Period_label","England","Minimum_english_regions","Mean_english_regions","Maximum_english_regions"]
#fieldnames=header
for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.EducationEmployeeExpenditure.insert(row)
