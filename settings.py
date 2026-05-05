import os
import psycopg2
from dotenv import load_dotenv
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG=True
# SECURITY WARNING: Modify this secret key if using in production!
SECRET_KEY = "<PLEASE PUT YOUR OWN KEY HERE IF NEEDED>"

DEFAULT_AUTO_FIELD='django.db.models.AutoField'
load_dotenv()
# https://dev.to/msnmongare/how-to-set-up-postgresql-database-with-a-django-application-4j17
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        # "OPTIONS": {"options": "-c search_path=beerme3"},
        "NAME": "beerme3",
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": "red-barn",
        # "PORT": "5432",
        # "OPTIONS": {"options": "-c search_path=mypicks1"},
    }
}

INSTALLED_APPS = ("db",)
