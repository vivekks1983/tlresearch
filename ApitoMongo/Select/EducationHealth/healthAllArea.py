from pymongo import MongoClient
from datetime import datetime
import requests
import json
import time

client = MongoClient()
db = client.test


collection = db['HHAged25To30AllUK']
cursor = collection.find({})
for document in cursor:
	print(document)


