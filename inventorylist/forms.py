from django import forms
from . models import Inventory

class Add_inventoryForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'Please enter the  description'}))
	unit_measure = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	no_of_units = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	period_of_measure = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	purchased_inventory = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	usage = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
	closing_inventory = forms.IntegerField(widget=forms.HiddenInput(attrs={'class':'form-control'}))
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
		# 'closing_inventory'
		]
