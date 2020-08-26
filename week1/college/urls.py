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
         views.stream_delete, name='stream_delete')
]
