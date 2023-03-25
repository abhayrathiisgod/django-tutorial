from django.urls import path
from . import views

urlpatterns =[
    #root url
    path('',views.index,name ='index'),
    path('counter',views.counter, name='counter'),
    path('register',views.register, name='register')
]