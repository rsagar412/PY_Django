from django.shortcuts import render, HttpResponse

def index(request):

    context = {
        'variable': "This is a defined variable demo from views page using the context dict. It is declared using {{variable}} in the index.html file"
    }
    # return HttpResponse("This is the homepage of the Django WebApp")
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse("this is the about page")

def services(request):
    return HttpResponse("this is the service page")

def contact(request):
    return HttpResponse("this is the contact page")
# Create your views here.
