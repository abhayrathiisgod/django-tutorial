from django.urls import path
from . import views

urlpatterns =[
    #root url
    path('',views.index,name ='index')

]