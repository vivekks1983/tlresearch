import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient
#CSV to JSON Conversion
csvfile = open('/home/ubuntu/project/ApiToMongo/Insert/LG/data/MortalityRateCausePreventable.csv', 'r')
reader = csv.DictReader( csvfile )
mongo_client=MongoClient() 
db=mongo_client.test
db.MortalityRatePerson.drop()
header= ["Indicator_ID","Indicator_Name","Parent_Code","Parent_Name","Area_Code","Area_Name","Area_Type","Sex","Age","Category_Type","Category","Time_period","Value","Lower_CI_limit","Upper_CI_limit","Count","Denominator","Value_note","Recent_Trend","Compared_to_England_value_or_percentiles","Compared_to_subnational_parent_value_or_percentiles" ]
#fieldnames=header
for each in reader:
    row={}
    for field in header:
        row[field]=each[field]

    db.MortalityRatePerson.insert(row)
