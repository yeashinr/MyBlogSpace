from django.shortcuts import render

# Create your views here.
post =[
    {
        'author'        : 'Yeashin',
        'title'         : 'Blog 1',
        'content'       : 'My First Blog',
        'date_posted'   : 'Jan 23, 2019'
    }
]

def home(request):
    context = {'posts': post}
    return render(request,'Blog/home.html',context)