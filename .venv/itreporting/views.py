from django.shortcuts import render


def home(request):
    
    return render(request, 'itreporting/home.html')

def about(request):
    
    return render(request, 'itreporting/about.html')

def contact(request):
    
    return render(request, 'itreporting/contact.html')

def moduleslist(request):
    
    return render(request, 'itreporting/modulelist.html')

# Create your views here.
