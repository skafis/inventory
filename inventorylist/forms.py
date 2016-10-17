from django import forms
from . models import Inventory

class Add_inventoryForm(forms.ModelForm):
	class Meta:
		model= Inventory
		fields = [
		'name',
		'description',
		'unit_measure',
		'no_of_units',
		'period_of_measure',
		'purchased_inventory',
		'usage',
		'closing_inventory'
		]
