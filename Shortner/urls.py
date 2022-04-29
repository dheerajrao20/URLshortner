from django.urls import path 
from Shortner import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
]