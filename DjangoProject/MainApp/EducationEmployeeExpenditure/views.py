# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from models import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from fusioncharts import FusionCharts
import datetime
from pymongo import MongoClient

def index(request):

	print(request)

	client = MongoClient()
	db = client.test
	collection = db['EducationEmployeeExpenditure']
	cursor = list(collection.find({}, {'_id': False}))
	category = [] 
	englandList = []
	maxList = []
	meanList = []
	minList = []

	dataSource = {}

	dataSource['chart'] = { 
		"caption": "Education Employee Expenditure",
		"xAxisname": "Year",
		"yAxisName": "Employee Expenditure",
		"theme": "zune"
	}

	for label in cursor:
		category.append({"label":label["Period_label"]})

	for englandData in cursor:
		englandList.append({"value":englandData["England"]})

	for maxData in cursor:
		maxList.append({"value":maxData["Maximum_english_regions"]})

	for meanData in cursor:
		meanList.append({"value":meanData["Mean_english_regions"]})

	for minData in cursor:
		minList.append({"value":minData["Minimum_english_regions"]})

	dataSource["categories"] = [{ "category":  category  }]

	dataSource["dataset"] = [{
		"seriesname": "England Data",
		"data": englandList
		}, {
		"seriesname": "Maximum English Regions",
		"data": maxList
		}, {
		"seriesname": "Mean of English Regions",
		"data": meanList
		}, {
		"seriesname": "Minimum of English Regions",
		"data": minList
		}    
	]

	column2d = FusionCharts("mscolumn3d", "ex1", "1200", "600", "chart-1", "json",dataSource)

	return render(request, 'index.html', {'output': column2d.render()})
