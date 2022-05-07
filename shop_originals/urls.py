""" url for shop_originals """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_originals, name='shop_originals'),
]
