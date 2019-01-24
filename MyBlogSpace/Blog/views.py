from django.shortcuts import render
from .models import Post

# Create your views here.


def home(request):
    context = {'posts': Post.objects.all() }
    print(context)
    return render(request,'Blog/home.html',context)