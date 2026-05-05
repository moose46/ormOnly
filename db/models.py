from django.db import models
from django.utils import timezone

# Create your models here.
class Person(models.Model):

	name = models.CharField(
		max_length=50,
		blank=False
	)
	age = models.IntegerField()
	birth_date = models.DateTimeField(
		blank=False
	)
