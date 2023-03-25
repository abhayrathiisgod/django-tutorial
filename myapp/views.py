from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Feature
# Create your views here.
def index(request):
    # cant put all in here ->>>>> return HttpResponse('<h1>I am batman!</h1>')
    #name= 'Abhay Rathi'

    # now we need name from the database so
    #name = user.name
    #good practice is to make dictionary
    
    features = Feature.objects.all()

    context = {
        'name': 'Abhay Rathi',
        'age':23,
        'nationality':'Nepalese'
    }
    return render(request,'index.html',{'features': features})   # like dictionary ->>{key:value}

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        password2 = request.POST['password2']
        email = request.POST['email']
        password = request.POST['password']

        #if password ==  password2:
            #return




    return render(request,'register.html')


def counter(request):
    text = request.POST['text']  # text????? ---> from the html form pa
    ans = len((text.split()))
    return render(request,'index.html',{'ans':ans})

