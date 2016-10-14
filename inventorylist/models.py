from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Inventory(models.Model):
	name = models.CharField(max_length=140)
	description = models.TextField()
	unit_measure = models.CharField(max_length=100)
	no_of_units = models.IntegerField(default=100)
	period_of_measure = models.CharField(max_length=100)