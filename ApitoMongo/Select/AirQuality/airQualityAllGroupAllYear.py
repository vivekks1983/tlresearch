from pymongo import MongoClient
from datetime import datetime
import requests
import json
import time

client = MongoClient()
db = client.test
collection = db['AirQualityAllGroupAllYear']
cursor = collection.find({})
print(cursor)
for document in cursor:
	print(document)
