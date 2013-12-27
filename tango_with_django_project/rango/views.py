from django.shortcuts import render

# Create your views here.

from django.http import Httpresponse

def index(request):
	return HttpResponse("Rango says HELLO WORLD.")
