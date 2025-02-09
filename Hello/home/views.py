from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("This is the homepage of the Django WebApp")
# Create your views here.
