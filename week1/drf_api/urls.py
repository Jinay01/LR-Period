from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'student', views.StudentViewSet)
router.register(r'stream', views.StreamViewSet)
router.register(r'college', views.CollegeViewSet)


urlpatterns = [
    # college section
    path('colleges', views.colleges, name='colleges'),
    path('college-details/<str:pk>', views.collegeDetails, name="college-details"),
    path('college-update/<str:pk>', views.collegeUpdate, name='college-update'),
    path('college-stream-delete/<str:pk>/<str:pk2>', views.collegeStreamDelete,
         name='college-stream-delete'),

    # college and stream method 2
    path('', include(router.urls)),


    # stream section
    path('streams', views.streams, name='streams'),
    path('stream-add', views.streamNew, name='stream-add'),
    path('stream-update/<str:pk>', views.streamUpdate, name='stream-update'),
    path('stream-delete/<str:pk>', views.streamDelete, name='stream-delete'),
]
