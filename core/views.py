from django.shortcuts import render
from .models import *
# Create your views here.
def info(request):
    posts = Posts.objects.all()
    feature = Featured.objects.all()
    silder = MainSilder.objects.all()
    starts = StartSlider.objects.all()
    context = {
        'posts':posts,
        'feature':feature,
        'silder':silder,
        'starts':starts
    }
    return render (request, 'index.html', context)
