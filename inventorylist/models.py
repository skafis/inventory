from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Inventory(models.Model):
	name = models.CharField(max_length=140)
	description = models.TextField(null=True)
	unit_measure = models.CharField(max_length=10)
	no_of_units = models.IntegerField()
	period_of_measure = models.CharField(max_length=100)
	purchased_inventory = models.IntegerField()
	usage = models.IntegerField()
	closing_inventory = models.IntegerField(null=True)

	# def _get_total(self):
	# 	"Returns the total"
	# 	return self.no_of_units * self.purchased_inventory
		
	# closing_inventory = property(_get_total)