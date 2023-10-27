from django.shortcuts import render
from .models import *
# Create your views here.
def info(request):
    posts = Posts.objects.all()
    context = {
        'posts':posts
    }
    return render (request, 'index.html', context)