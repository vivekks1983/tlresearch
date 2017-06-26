# This Script inserts data of Air Quality for All Year , All Group
from pymongo import MongoClient
from datetime import datetime
import requests
import json
import time
import codecs

client = MongoClient()
db = client.test


headers ={
        'Accept': 'application/json'
}

response = requests.get("http://api.erg.kcl.ac.uk/AirQuality/Annual/MonitoringObjective/GroupName=All/Json",headers=headers)

if response.status_code == 200:
	target = open("/home/ubuntu/project/ApiToMongo/AirQualityAllGroupAllYear.json", 'w')
	target.truncate()
	target.write(response.text)
	target.close()
	jsonResponse = json.load(codecs.open('/home/ubuntu/project/ApiToMongo/AirQualityAllGroupAllYear.json', 'r', 'utf-8-sig'))
	result = db.AirQualityAllGroupAllYear.insert_one(jsonResponse)
