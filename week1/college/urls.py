from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('registration', views.regis, name='registration'),
    path('loginpage', views.loginPage, name="loginpage"),
    path('logout', views.logoutUser, name='logout'),
    path('college_settings/<str:pk>',
         views.college_settings, name='college_settings'),
    path('stream_delete/<str:pk>/<str:pk1>',
         views.stream_delete, name='stream_delete'),
    path('update_stream/<str:pk>', views.update_stream, name='update_stream'),
    path('delete_college/<str:pk>', views.delete_college, name='delete_college'),
]
