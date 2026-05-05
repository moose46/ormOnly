# https://dev.to/ivanyu2021/using-django-orm-only-without-web-server-1oc8

##############################
## Django specific settings (Please this BEFORE import model class)
##############################
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()
##############################

import datetime
from db.models import Person

print("Project started!!")
person = Person()
person.name = 'John Doe'
person.age = 30
person.birth_date = datetime.datetime(1963, 2, 5)
person.save()
print("Saved!!")
