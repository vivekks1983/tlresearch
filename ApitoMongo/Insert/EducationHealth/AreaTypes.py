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


response = requests.get("http://webservices.esd.org.uk/areaTypes?ApplicationKey=PDdYFFDExbdVjrNXzEHyVmjIWudKInpKXuHajaUw&Signature=NaY2S1B4aAsozuc1+0A1sgT0r3Q=",headers=headers)
if response.status_code == 200:
	jsonResponse = json.loads(response.text)
	result = db.AreaTypes.insert_one(jsonResponse)
	print(result)

