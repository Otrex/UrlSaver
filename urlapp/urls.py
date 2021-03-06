from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index, name= "index"),
    path("get/", views.geturl, name= "get"),
    path("delete/<int:tid>", views.deleteUrl, name= "deleteUrl"),
]