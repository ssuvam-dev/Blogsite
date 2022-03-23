from unicodedata import category
from urllib import request
from django.shortcuts import render,get_object_or_404
from .models import Category,Blogpost
# Create your views here.
def index(request):
    categories=Category.objects.all()
    blogpost=Blogpost.objects.all().order_by('-created')
    context={'posts':blogpost,'categories':categories}
    return render(request,'index.html',context)

def categorydetails(request,category_slug):
    page='category'
    category=get_object_or_404(Category,slug=category_slug)
    context={'page':page,'category':category}
    return render(request,'index.html',context)

def postdetails(request,post_slug):
    posts=get_object_or_404(Blogpost,slug=post_slug)
    context={'post':posts,}
    return render(request,'post_details.html',context)

