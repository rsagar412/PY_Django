from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("This is the homepage of the Django WebApp")

def about(request):
    return HttpResponse("this is the about page")

def services(request):
    return HttpResponse("this is the service page")

def contact(request):
    return HttpResponse("this is the contact page")
# Create your views here.
