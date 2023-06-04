from django.urls import path
from . import views


urlpatterns = [
    path("lista/",views.index,name="index"),
    path("create/", views.create, name="create"),
    path("", views.ola),
    path("k/", views.k),
    
]