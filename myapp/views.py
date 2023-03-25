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

        if password ==  password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already used')
                return redirect('register')
            else:
                # all correct pa
                user =User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Passwords are not same!')
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username)

        if user  is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials invalid')
            return redirect('login')
    else:
        return render(request,'login.html')

def counter(request):
    text = request.POST['text']  # text????? ---> from the html form pa
    ans = len((text.split()))
    return render(request,'index.html',{'ans':ans})

