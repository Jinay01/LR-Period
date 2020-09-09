from django.urls import path
from . import views

urlpatterns = [
    # college section
    path('colleges', views.colleges, name='colleges'),
    path('college-details/<str:pk>', views.collegeDetails, name="college-details"),
    # stream section
    path('streams', views.streams, name='streams'),
    path('stream-add', views.streamNew, name='stream-add'),
    path('stream-update/<str:pk>', views.streamUpdate, name='stream-update'),
    path('stream-delete/<str:pk>', views.streamDelete, name='stream-delete'),
]
