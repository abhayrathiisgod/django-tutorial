from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # cant put all in here ->>>>> return HttpResponse('<h1>I am batman!</h1>')
    #name= 'Abhay Rathi'

    # now we need name from the database so
    #name = user.name
    #good practice is to make dictionary
    context = {
        'name': 'Abhay Rathi',
        'age':23,
        'nationality':'Nepalese'
    }
    return render(request,'index.html')   # like dictionary ->>{key:value}

def counter(request):
    text = request.POST['text']  # text????? ---> from the html form pa
    ans = len((text.split()))
    return render(request,'index.html',{'ans':ans})

