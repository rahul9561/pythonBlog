from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render 
from .models import Post

def index(request):
    Posts=Post.objects.all()
    return render(request,"index.html",{"posts":Posts})

