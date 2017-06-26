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


response = requests.get("http://webservices.esd.org.uk/data?value.valueType=raw&metricType=342&area=AllSingleTierAndDistrictLaInUK&period=latest&columnGrouping=metricType&columnGrouping=period&columnGrouping=valueType&rowGrouping=area",headers=headers)
if response.status_code == 200:
	jsonResponse = json.loads(response.text)
	result = db.HHAged25To30AllUK.insert_one(jsonResponse)
	print(result)

