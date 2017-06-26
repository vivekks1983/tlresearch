# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mongoengine import *
from MongoToDjango.settings import DBNAME
 
connect('test')
 
class Educationemployeeexpenditur(Document):
    title = StringField(max_length=120, required=True)
    content = StringField(max_length=500, required=True)
    last_update = DateTimeField(required=True)

class Educationemployeeexpenditure(Document):
    Mean_english_regions = IntField()
    Maximum_english_regions = IntField()
    Period_identifier = StringField()
    Minimum_english_regions = IntField()
    England = IntField()
    Period_label = StringField()
# Create your models here.
