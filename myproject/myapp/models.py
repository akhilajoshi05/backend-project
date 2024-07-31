# from django.db import models

# Create your models here.
# myapp/models.py

from django.db import models
from db_connection import db

myapp_collection = db['myapp']

# class Student(models.Model):
#     name = models.CharField(max_length=200)
#     courses = models.JSONField()
#     additional_info = models.JSONField()

#     def __str__(self):
#         return self.name
