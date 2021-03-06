from django.urls import path
from . import views

app_name = 'up'

urlpatterns = [
	path("", views.index, name = "index"),
	path("get/", views.get, name = "get"),
	path("delete/<int:tid>", views.delete, name = "delete"),
]