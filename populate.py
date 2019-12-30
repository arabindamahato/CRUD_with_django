# setting the django 
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","models.settings")


# setting up the django feature
import django 
django.setup()

from faker import Faker  # get the fake data
from myapp.models import *
import random # to choose data randomly

f = Faker()
topics = ["Music","Sports","Social Media","Movies","News","Aggregater","Educational"]
def add_topic(top_name): # top_name = database field name
    t = Topic.objects.get_or_create(top_name = top_name)[0] # Topic = model name
    t.save()
    return t

def add_webpage(top_name, name, url): # arguments are the field name of webpage table
    t = add_topic(top_name)
    w = Webpage.objects.get_or_create(top_name=t, name=name, url=url)[0] 
    w.save()
    return w

def add_access_details(top_name, name, url, date):
    w = add_webpage(top_name, name, url)
    a = Access_Details.objects.get_or_create(name=w, date=date)[0]
    a.save()

def add_data():
    top_name = random.choice(topics) # picks the random element from the list
    name = f.first_name()  # fake name
    url = f.url()  # fake url
    date = f.date() # fake date
    add_access_details(top_name, name, url, date)


if __name__ == "__main__":
    N = int(input("Enter the number of fake data that you wanted to populate"))
    for i in range(N):
        add_data()


















