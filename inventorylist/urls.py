from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.view_inventory, name='view'),
	url(r'^add/$', views.add_inventory, name='add')
]