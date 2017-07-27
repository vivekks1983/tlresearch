from flask import render_template
from pymongo import MongoClient
from flask import jsonify
from app import app
import json

@app.route('/AirQuality/<data>')
def AirQuality(data):
	client = MongoClient()
	db = client.test

	if data=="HourlyMonitoringIndexAllGroup":
		collection = db['HourlyMonitoringIndexAllGroup']
	elif data=="SpeciesInformation":
		collection = db['SpeciesInformation']
	elif data=="MonitoringSites":
		collection = db['MonitoringSites']
	elif data=="MonitoringLocalAuthority":
		collection = db['MonitoringLocalAuthority']
	elif data=="Objective":
		collection = db['Objective']
	elif data=="IndexHealthAdvice":
		collection = db['IndexHealthAdvice']
	elif data=="AirQualityAllGroupAllYear":
		collection = db['AirQualityAllGroupAllYear']
	elif data=="AirQuality2009AllGroup":
		collection = db['AirQuality2009AllGroup']
	elif data=="AirQuality2008AllGroup":
		collection = db['AirQuality2008AllGroup']
	elif data=="AirQuality2007AllGroup":
		collection = db['AirQuality2007AllGroup']
	elif data=="AirQuality2006AllGroup":
		collection = db['AirQuality2006AllGroup']
	elif data=="AirQuality2005AllGroup":
		collection = db['AirQuality2005AllGroup']
	elif data=="AirQuality2004AllGroup":
		collection = db['AirQuality2004AllGroup']
	elif data=="AirQuality2003AllGroup":
		collection = db['AirQuality2003AllGroup']
	elif data=="AirQuality2002AllGroup":
		collection = db['AirQuality2002AllGroup']
	elif data=="AirQuality2001AllGroup":
		collection = db['AirQuality2001AllGroup']
	elif data=="AirQuality2000AllGroup":
		collection = db['AirQuality2000AllGroup']
	elif data=="AirQuality1999AllGroup":
		collection = db['AirQuality1999AllGroup']
	elif data=="AirQuality1998AllGroup":
		collection = db['AirQuality1998AllGroup']
	elif data=="AirQuality1997AllGroup":
		collection = db['AirQuality1997AllGroup']
	elif data=="AirQuality1996AllGroup":
		collection = db['AirQuality1996AllGroup']
	else:
		return render_template('error.html',
			endpoint=data)

	cursor = list(collection.find({}, {'_id': False}))
	response = app.response_class(
		response=json.dumps(cursor),
		status=200,
		mimetype='application/json'
		)
	return response



@app.route('/LG/<data>')
def LG(data):
	client = MongoClient()
	db = client.test

	if data=="AreaTypes":
		collection = db['AreaTypes']
	elif data=="DetailedAreaDesciption":
		collection = db['DetailedAreaDesciption']
	elif data=="HHAged25To30AllUK":
		collection = db['HHAged25To30AllUK']
	elif data=="PublicHealthOutcomes":
		collection = db['PublicHealthOutcomes']
		cursor = list(collection.find({}, {'_id': False}))
		return render_template("PublicHealthOutcomes.html",
				title='Education Head Count',
				posts=cursor)
	elif data=="InfantMortality":
		collection = db['InfantMortality']
		cursor = list(collection.find({}, {'_id': False}))
		return render_template("InfantMortality.html",
				title='Education Head Count',
				posts=cursor)
	elif data=="AboveFiveMortality":
		collection = db['AboveFiveMortality']
		cursor = list(collection.find({}, {'_id': False}))
		return render_template("AboveFiveMortality.html",
				title='Education Head Count',
				posts=cursor)
	elif data=="MortalityRatePerson":
		collection = db['MortalityRatePerson']
		cursor = list(collection.find({}, {'_id': False}))
		return render_template("MortalityRatePerson.html",
				title='Education Head Count',
				posts=cursor)
	elif data=="EducationHeadCount":
		collection = db['EducationHeadCount']
		cursor = list(collection.find({}, {'_id': False}))
		return render_template("EducationHeadCount.html",
				title='Education Head Count',
				posts=cursor)
	elif data=="EducationEmployeeExpenditure":
		collection = db['EducationEmployeeExpenditure']
		cursor = list(collection.find({}, {'_id': False}))
		return render_template("EducationEmployeeExpenditure.html",
				title='Education Employee Expenditure',
				posts=cursor)
	else:
		return render_template('error.html',
			endpoint=data)

	cursor = list(collection.find({}, {'_id': False}))
	response = app.response_class(
		response=json.dumps(cursor),
		status=200,
		mimetype='application/json'
		)
	return response



@app.route('/')
@app.route('/index')
def index():
		return render_template("index.html",
				title='Trilateral Research Data')
