from django.urls import path
from . import views
#from django.conf.urls import handler404
from django.conf import settings
# from .views import student_message, SendMessageView, GetMessagesView 
urlpatterns=[
    path('', views.home, name='home'),
]  
 
 