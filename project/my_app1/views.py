from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1(request):
    return HttpResponse("<h1>hello to cybrom...</h1>")
