from django.shortcuts import render
from .models import Blog

# Create your views here.
def home(request): 

    return render(request,'home.html')


def add(request):
    vtitle=request.POST["title"]
    vdescription=request.POST["description"]
    blogs=Blog(title=vtitle,description=vdescription)
    blogs.save()
    allblogs=Blog.objects.all().order_by('-id')
    return render(request,'result.html',{'result':allblogs})

def delete(request):

    Blog.objects.filter(id=request.POST["id"]).delete()
    allblogs = Blog.objects.all().order_by('-id')
    return render(request, 'result.html', {'result':allblogs})

def edit(request):
    vid=request.POST["id"]
    vtitle=request.POST["title"]
    vdescription=request.POST["description"]
    blogs=Blog(id=vid,title=vtitle,description=vdescription)
    blogs.save()
    allblogs=Blog.objects.all().order_by('-id')
    return render(request,'result.html',{'result':allblogs})

def editrow(request):
    
    allblogs=Blog.objects.all().filter(id=request.POST["id"])
    return render(request,'edit.html',{'result':allblogs})