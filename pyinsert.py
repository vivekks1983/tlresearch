from pymongo import MongoClient
from datetime import datetime
import requests
import json
import time

client = MongoClient()
db = client.test


headers ={
        'Accept': 'application/json'
}


response = requests.get("http://api.erg.kcl.ac.uk/AirQuality/Annual/MonitoringObjective/GroupName=All/Year=1996/Json",headers=headers)
if response.status_code == 200:
	jsonResponse = json.loads(response.text)
	result = db.AirQuality1996AllGroup.insert_one(jsonResponse)
	print(result)

response = requests.get("http://api.erg.kcl.ac.uk/AirQuality/Annual/MonitoringObjective/GroupName=All/Year=1997/Json",headers=headers)
if response.status_code == 200:
	jsonResponse = json.loads(response.text)
	result = db.AirQuality1997AllGroup.insert_one(jsonResponse)
	print(result)

response = requests.get("http://api.erg.kcl.ac.uk/AirQuality/Annual/MonitoringObjective/GroupName=All/Year=1998/Json",headers=headers)
if response.status_code == 200:
	jsonResponse = json.loads(response.text)
	result = db.AirQuality1998AllGroup.insert_one(jsonResponse)
	print(result)

response = requests.get("http://api.erg.kcl.ac.uk/AirQuality/Annual/MonitoringObjective/GroupName=All/Year=1999/Json",headers=headers)
if response.status_code == 200:
	jsonResponse = json.loads(response.text)
	result = db.AirQuality1999AllGroup.insert_one(jsonResponse)
	print(result)


response = requests.get("http://api.erg.kcl.ac.uk/AirQuality/Annual/MonitoringObjective/GroupName=All/Year=2000/Json",headers=headers)
if response.status_code == 200:
	jsonResponse = json.loads(response.text)
	result = db.AirQuality2000AllGroup.insert_one(jsonResponse)
	print(result)


response = requests.get("http://api.erg.kcl.ac.uk/AirQuality/Annual/MonitoringObjective/GroupName=All/Year=2001/Json",headers=headers)
if response.status_code == 200:
	jsonResponse = json.loads(response.text)
	result = db.AirQuality2001AllGroup.insert_one(jsonResponse)
	print(result)


response = requests.get("http://api.erg.kcl.ac.uk/AirQuality/Annual/MonitoringObjective/GroupName=All/Year=2002/Json",headers=headers)
if response.status_code == 200:
	jsonResponse = json.loads(response.text)
	result = db.AirQuality2002AllGroup.insert_one(jsonResponse)
	print(result)


response = requests.get("http://api.erg.kcl.ac.uk/AirQuality/Annual/MonitoringObjective/GroupName=All/Year=2003/Json",headers=headers)
if response.status_code == 200:
	jsonResponse = json.loads(response.text)
	result = db.AirQuality2003AllGroup.insert_one(jsonResponse)
	print(result)


response = requests.get("http://api.erg.kcl.ac.uk/AirQuality/Annual/MonitoringObjective/GroupName=All/Year=2004/Json",headers=headers)
if response.status_code == 200:
	jsonResponse = json.loads(response.text)
	result = db.AirQuality2004AllGroup.insert_one(jsonResponse)
	print(result)


response = requests.get("http://api.erg.kcl.ac.uk/AirQuality/Annual/MonitoringObjective/GroupName=All/Year=2005/Json",headers=headers)
if response.status_code == 200:
	jsonResponse = json.loads(response.text)
	result = db.AirQuality2005AllGroup.insert_one(jsonResponse)
	print(result)


response = requests.get("http://api.erg.kcl.ac.uk/AirQuality/Annual/MonitoringObjective/GroupName=All/Year=2006/Json",headers=headers)
if response.status_code == 200:
	jsonResponse = json.loads(response.text)
	result = db.AirQuality2006AllGroup.insert_one(jsonResponse)
	print(result)


response = requests.get("http://api.erg.kcl.ac.uk/AirQuality/Annual/MonitoringObjective/GroupName=All/Year=2007/Json",headers=headers)
if response.status_code == 200:
	jsonResponse = json.loads(response.text)
	result = db.AirQuality2007AllGroup.insert_one(jsonResponse)
	print(result)


response = requests.get("http://api.erg.kcl.ac.uk/AirQuality/Annual/MonitoringObjective/GroupName=All/Year=2008/Json",headers=headers)
if response.status_code == 200:
	jsonResponse = json.loads(response.text)
	result = db.AirQuality2008AllGroup.insert_one(jsonResponse)
	print(result)


