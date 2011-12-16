import datetime

from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=50) #longest has 45 chars
    definition = models.TextField()
    context = models.TextField()
    has_memorized =models.BooleanField(default=False)
    #TODO: figure out db_index
    time_created = models.DateTimeField(default=datetime.datetime.now, db_index=True) 
    time_modified = models.DateTimeField(default=datetime.datetime.now) 
