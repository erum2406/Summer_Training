from django.shortcuts import render
from django.http import HttpResponse
from . models import director_login

# Create your views here.
def director(request):
    return render(request,'director.html')
    
def dlogin(request):
    duser=request.POST['duser']
    dpass=request.POST['dpass']
    res=director_login.objects.filter(duser=duser, dpass=dpass)
    if len(res)==1:
        return redirect('home')
    else:
        return render(request, 'director.html',{'error':'Username or Password is Incorrect.'})
        
def home(request):
    return render(request, 'home.html')