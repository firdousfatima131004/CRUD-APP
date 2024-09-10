from django.contrib import redirects
from django.shortcuts import redirect,render
from django.contrib.auth import login,authenticate
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method =="POST":
        uname=request.POST['us_name']
        ueml=request.POST['e_mail']
        upas=request.POST['u_pass']
        uobj=Crudprofiles(username=uname,email=ueml,password=upas)
        uobj.save()
    return render(request,'register.html')

def adminpage(request):
    if request.method =="POST":
        uname=request.POST['usname']
        upass=request.POST['uspass']
        user=authenticate(request,username=uname,password=upass)
        print(user)
        if user is not None:
            login(request,user)
            
            return redirect("/details")
        else:
            return HttpResponse("Invalid Credentials")

    return render(request,'adminpage.html')
@login_required
def detailspage(request):
    usermo=Crudprofiles.objects.all()
    return render(request,'details.html',{'usermo':usermo})
def deleteid(request, id):
    try:
        data = Crudprofiles.objects.get(id=id)
        data.delete()
        messages.success(request,'Data deleted successfully')
        return redirect('/details')
    except Crudprofiles.DoesNotExist:
        # Handle the case where the object doesn't exist
        # Redirect to an appropriate page or show an error message
        return HttpResponse("User does not exist")  # Or redirect to an error page