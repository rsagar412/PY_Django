from django.shortcuts import render, HttpResponse

def index(request):

    context = {
        'variable': "This is a defined variable demo from views page using the context dict. It is declared using {{variable}} in the index.html file"
    }
    # return HttpResponse("This is the homepage of the Django WebApp")
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
     return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')
# Create your views here.
