from django.db import models
from myapp.models import *

# Create your models here.


class Topic(models.Model):
    top_name = models.CharField(max_length=120, primary_key=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    top_name = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, primary_key=True)
    url = models.URLField(unique=True)

    def __str__(self):   
        return self.name 

class Access_Details(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField(unique=True)

    def __str__(self):
        return str(self.date)
    
    
    