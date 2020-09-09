from django.urls import path
from . import views

urlpatterns = [
    path('colleges', views.colleges, name='colleges'),
    path('streams', views.streams, name='streams'),
]
