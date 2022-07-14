from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
  return HttpResponse("Hello")


def signup(request):
  return render(request, "app/signup.html")


def signin(request):
  return render(request, "app/signin.html")


def signout(request):
  pass
