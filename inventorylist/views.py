from django.shortcuts import render

import inventorylist.class_views.inventory_listing as inventory


# Create your views here.
def add_inventory(request, template_name='add_inventory.html'):
	return inventory.add_inventory(request, template_name=template_name)

def  view_inventory(request, template_name='inventory.html'):
	return inventory.view_inventory(request, template_name=template_name)