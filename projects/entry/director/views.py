from django.shortcuts import render, redirect
from . models import director_login
from gaurd.models import gaurds
from gaurd.models import guest_entries

# Create your views here.
def director(request):
    if request.session.get('duser'):
        return redirect('home')
    else:
        return render(request,'director.html')
    
    
def dlogin(request):
    duser=request.POST['duser']
    dpass=request.POST['dpass']
    
    res = director_login.objects.filter(duser=duser, dpass=dpass)
    if len(res)==1:
        request.session['duser']=res[0].duser
        return redirect('home')
    else:
        return render(request, 'director.html',{'error':'Username or Password is Incorrect.'})
        
def home(request):
    if request.session.get('duser'):
        return render(request,'home.html')
    else:
        return redirect('/director/')

def logout(request):
            del request.session['duser']
            return redirect('/director/')
            
def account(request):
    if request.session.get('duser'):
        return render(request,'account.html')
    else:
        return redirect('/director/')
        
def create_account(request):
    guser=request.POST['guser']
    gfname=request.POST['gfname']
    glname=request.POST['glname']
    gpass=request.POST['gpass']
    res=gaurds.objects.filter(guser=guser)
    if len(res)>0:
        return render(request,'account.html',{'msg':'Gaurd is already existing!!!'})
    else:
        a=gaurds(guser=guser, gfname=gfname, glname=glname, gpass=gpass)
        a.save()
        return render(request,'account.html',{'msg':'Account created successfully'})
        
def checked(request):
    res=guest_entries.objects.all()
    return render(request,'checked.html',{'res':res})