""" url for shopping basket """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
]