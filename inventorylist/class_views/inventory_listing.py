from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from inventorylist.models import Inventory
from inventorylist.forms import Add_inventoryForm


def create_inventory(request, template_name='add_inventory.html'):
	form = Add_inventoryForm(request.POST or None)
	ctx = {}
	ctx['form'] = form
	form.fields['closing_inventory'].initial = 20
	if request.method == "POST":
		if form.is_valid():
			instance = form.save(commit=False)
			closing_stock = (int(request.POST['no_of_units'])+int(request.POST['purchased_inventory']))-int(request.POST['usage'])
			instance.closing_inventory = closing_stock
			instance.save()

			print closing_stock
			return redirect('view')	
	return render(request, template_name, ctx)

def read_inventory(request, template_name='inventory.html'):
	inventory_list = Inventory.objects.all()
	ctx = {}
	# closing_stock = []
	# for items in Inventory.objects.all():
	# 	inventory_purchased =  items.purchased_inventory
	# 	inventory_open = items.no_of_units
	# 	used_items = items.usage
	# 	closing_ = (inventory_open + inventory_purchased) - used_items
	# 	closing_stock.append(closing_)
	# 	# ctx['closing_stock'].append(closing_stock)
	# 	# print closing_stock
	
	# # ctx['closing_stock'] = closing_stock 
	ctx['inventory_list'] = inventory_list

	return render(request, template_name, ctx)

def update_inventory(request, pk, template_name='add_inventory.html'):
	item = Inventory.objects.get(pk=pk)
	ctx = {}
	form = Add_inventoryForm(request.POST or None, instance=item)
	if form.is_valid():
		instance = form.save()
		return redirect('view')
	ctx['form']=form
	return render(request, template_name, ctx)

def delete_inventory(request, pk, template_name='inventory.html'):
	item = Inventory.objects.get(pk=pk)
	item.delete()
	return redirect('view')

def login_method(request, template_name='w.html'):
	return render(request, template_name)