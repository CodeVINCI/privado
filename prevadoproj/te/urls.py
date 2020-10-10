from django.urls import path, include
from . import views

urlpatterns = [
    path('customer/<int:customerid>/templates', views.customer,name='customer'),
]

