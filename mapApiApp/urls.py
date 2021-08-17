from django.urls import path
from . import views

app_name = "mapApi"

urlpatterns = [
    path('', views.home, name="home"),
]