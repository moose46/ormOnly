# https://dev.to/ivanyu2021/using-django-orm-only-without-web-server-1oc8

##############################
## Django specific settings (Please this BEFORE import model class)
##############################
import django
import os
try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    django.setup()
except Exception as e:
    exit(e.__str__())
##############################

import datetime
from db.models import Track

print("Project started!!")
track = Track()
track.name = 'Atlanta'
track.configuration = "oval"
track.length = 1.5
try:
	track.save()
except Exception as e:
    exit(e.__str__())

print("Saved!!")
