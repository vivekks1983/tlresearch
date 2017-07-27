from pymongo import MongoClient
from datetime import datetime
import requests
import json
import time

client = MongoClient()
db = client.test


collection = db['AirQuality1996AllGroup']
cursor = collection.find({})
for document in cursor:
	print(document)


collection = db['AirQuality1997AllGroup']
cursor = collection.find({})
for document in cursor:
	print(document)


collection = db['AirQuality1998AllGroup']
cursor = collection.find({})
for document in cursor:
	print(document)


collection = db['AirQuality1999AllGroup']
cursor = collection.find({})
for document in cursor:
	print(document)


collection = db['AirQuality2000AllGroup']
cursor = collection.find({})
for document in cursor:
	print(document)


collection = db['AirQuality2001AllGroup']
cursor = collection.find({})
for document in cursor:
	print(document)


collection = db['AirQuality2002AllGroup']
cursor = collection.find({})
for document in cursor:
	print(document)


collection = db['AirQuality2003AllGroup']
cursor = collection.find({})
for document in cursor:
	print(document)


collection = db['AirQuality2004AllGroup']
cursor = collection.find({})
for document in cursor:
	print(document)


collection = db['AirQuality2005AllGroup']
cursor = collection.find({})
for document in cursor:
	print(document)


collection = db['AirQuality2006AllGroup']
cursor = collection.find({})
for document in cursor:
	print(document)


collection = db['AirQuality2007AllGroup']
cursor = collection.find({})
for document in cursor:
	print(document)


collection = db['AirQuality2008AllGroup']
cursor = collection.find({})
for document in cursor:
	print(document)


collection = db['AirQuality2009AllGroup']
cursor = collection.find({})
for document in cursor:
	print(document)


