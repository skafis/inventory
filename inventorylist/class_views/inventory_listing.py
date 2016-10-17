from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from inventorylist.models import Inventory
from inventorylist.forms import Add_inventoryForm


def create_inventory(request, template_name='add_inventory.html'):
	form = Add_inventoryForm(request.POST or None)
	ctx = {}
	ctx['form'] = form

	if request.method == "POST":
		if form.is_valid():
			instance = form.save()
			return redirect('view')
	return render(request, template_name, ctx)

def read_inventory(request, template_name='inventory.html'):
	inventory_list = Inventory.objects.order_by('id')
	ctx = {}
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
