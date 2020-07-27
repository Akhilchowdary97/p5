from django.shortcuts import render
from django.http import HttpResponse
from math import factorial
# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome To Views Of An APP</h1>")
def home(request):
    return render(request,"myapp/home.html",{'name':"Akhil"})
def fact(request,n):
    n=int(n)
    return HttpResponse("<h3>Factorial is {}</h3>".format(factorial(n)))
def child(request):
    return render(request,"child.html")