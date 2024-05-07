from django.shortcuts import render


def home(request):
    
    return render(request, 'itreporting/home.html', {'title':
'Welcome'})

def about(request):
    
    return render(request, 'itreporting/about.html', {'title':
'About'})

def contact(request):
    
    return render(request, 'itreporting/contact.html', {'title':
'Contact'})

def moduleslist(request):
    
    return render(request, 'itreporting/modulelist.html', {'title':
'List of Modules'})

# Create your views here.
