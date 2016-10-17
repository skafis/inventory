from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.read_inventory, name='view'),
	url(r'^add/$', views.create_inventory, name='create'),
	url(r'^(?P<pk>\d+)/update$', views.update_inventory, name='update_inventory'),
	url(r'^(?P<pk>\d+)/delete$', views.delete_inventory, name='delete_inventory'),
	# url(r'^add/$', views.create_inventory, name='add')
]