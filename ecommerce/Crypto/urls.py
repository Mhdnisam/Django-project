from django.urls import path
from . import views

urlpatterns =[
path('',views.index),
path('register/',views.registerview,name='register'),
path('login/',views.loginview,name='login'),
path('about/',views.aboutview,name='about'),
path('help/',views.helpview,name='help'),
path('team/',views.teamview,name='team'),
]