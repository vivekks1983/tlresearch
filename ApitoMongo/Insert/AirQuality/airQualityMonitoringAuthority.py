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

response = requests.get("http://api.erg.kcl.ac.uk/AirQuality/Information/MonitoringLocalAuthority/GroupName=All/Json",headers=headers)

if response.status_code == 200:
	jsonResponse = json.loads(response.text)
	result = db.MonitoringLocalAuthority.insert_one(jsonResponse)
