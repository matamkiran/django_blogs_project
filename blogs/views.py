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
    allblogs=Blog.objects.all()
    return render(request,'result.html',{'result':allblogs})