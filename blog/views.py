from django.shortcuts import render, get_object_or_404
from .models import Blog 
# Create your views here.

def Allblog(request):
    blogs = Blog.objects
    return render(request, 'blog/myblog.html',{'blogs': blogs,'name': 'My Blog'})


def Detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'blog': detailblog})
