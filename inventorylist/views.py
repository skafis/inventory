from django.shortcuts import render

import inventorylist.class_views.inventory_listing as inventory


# Create your views here.
def create_inventory(request, template_name='add_inventory.html'):
	return inventory.create_inventory(request, template_name=template_name)

def  read_inventory(request, template_name='inventory.html'):
	return inventory.read_inventory(request, template_name=template_name)

def update_inventory(request, pk, template_name='add_inventory.html'):
	return inventory.update_inventory(request, pk, template_name=template_name)

def delete_inventory(request, pk, template_name="inventory.html"):
	return inventory.delete_inventory(request, pk, template_name=template_name)