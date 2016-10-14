from django.shortcuts import render
from django.core.urlresolvers import reverse

from inventorylist.models import Inventory
from inventorylist.forms import Add_inventoryForm

def add_inventory(request, template_name='inventory.html'):
	form = Add_inventoryForm(request.POST or None)
	ctx = {}
	ctx['form'] = form

	if request.method == "POST":
		if form.is_valid():
			instance = form.save()
			return redirect ('/')

	return render(request, template_name, ctx)
