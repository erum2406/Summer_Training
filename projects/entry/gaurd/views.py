from django.shortcuts import render, redirect
from . models import gaurds

# Create your views here.
def gaurd(request):
    if request.session.get('guser'):
        return redirect('ghome')
    else:
        return render(request,'gaurd.html')
    
def glogin(request):
    guser=request.POST['guser']
    gpass=request.POST['gpass']
    res=gaurds.objects.filter(guser=guser, gpass=gpass)
    if len(res)==1:
        request.session['guser']=res[0].guser
        return redirect('ghome')
    else:
        return render(request,'ghome.html',{'error':'Username or Password Incorrect!!!'})
        
def ghome(request):
    if request.session.get('guser'):
        return render(request,'ghome.html')
    else:
        return redirect('/gaurd/')