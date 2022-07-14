from django.shortcuts import render
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def home(request):
  return render(request, "app/index.html")


def signup(request):
  
  if request.method == "POST":
    #username = request.POST.get('username')
    username = request.POST['username']
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    pass1 = request.POST['pass1']
    pass2 = request.POST['pass2']
    
    myuser = User.objects.create(username, email, pass1)
    myuser.first_name = fname
    myuser.last_name = lname
    
    myuser.save()
    
    messages.success(request, "Your account has been successfully created.")
    
    return redirect('signin')
    
  return render(request, "app/signup.html")


def signin(request):
  return render(request, "app/signin.html")


def signout(request):
  pass
