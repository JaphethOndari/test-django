from django.shortcuts import render
from .models import Post

# Create your views here.

# from django.http import HttpResponse

# def hello(requests):
#     return HttpResponse("Welcome to my django app")

def home(request):
    context = {
        'title': 'homepage',
        'description': 'welcome to the homepage'
    }
    return render(request, 'home.html', context)
    
def contactus(request):
    context = {
        'title': 'contactus',
        'description': 'welcome to the homepage'
    }
    return render(request, 'contactus.html', context)
    
def about(request):
    context = {
        'title': 'about',
        'description': 'welcome to the homepage'
    }
    return render(request, 'about.html', context)

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})