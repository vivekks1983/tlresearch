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


response = requests.get("http://webservices.esd.org.uk/areaTypes/verbose?ApplicationKey=PDdYFFDExbdVjrNXzEHyVmjIWudKInpKXuHajaUw&Signature=eUlHQWfuw++mn8s16OuQH7aLBkA=",headers=headers)
if response.status_code == 200:
	jsonResponse = json.loads(response.text)
	result = db.DetailedAreaDesciption.insert_one(jsonResponse)
	print(result)

