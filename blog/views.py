from django.shortcuts import render
# imoprt blog , cooment
from .models import Blog, Comment
# import user
from django.contrib.auth.models import User
# import pagenator
from django.core.paginator import Paginator
# import redirct
from django.shortcuts import redirect

import re
# Create your views here.

def blog(request):
   # blog def
    blog = Blog.objects.filter(title__regex=r'[A-Za-z]+')
    paginator = Paginator(blog, 8) # Show 8 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'blogs': page_obj}
    return render(request, 'blog.html',context)

def addblog(request):
    # add blog
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        image = request.FILES['image']
        user = User.objects.get(id=request.user.id)
        blog = Blog(user=user, title=title, body=body, image=image)
        blog.save()
        return redirect('blog')
    return render(request, 'addblog.html')

def blogdetails(request,id):
    #single blog 
    id=id
    blog = Blog.objects.get(id=id)
    # comment
    comment = Comment.objects.filter(blog=blog)
    context = {'blog': blog, 'comments': comment}
    if request.method == 'POST':
        comment = request.POST['comment']
        user = User.objects.get(id=request.user.id)
        blog = Blog.objects.get(id=id)
        comment = Comment(user=user, blog=blog, comment=comment)
        comment.save()
        return redirect('blog:blogdetails', id)
    return render(request, 'single-post.html', context)


#ar
def blog_ar(request):
    # blog def
     blog = Blog.objects.filter(title__regex=r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+')
     paginator = Paginator(blog, 8) # Show 8 contacts per page.
     page_number = request.GET.get('page')
     page_obj = paginator.get_page(page_number)
     context = {'blogs': page_obj}
     return render(request, 'blog-ar.html',context)
 
def addblog_ar(request):
        # add blog
        if request.method == 'POST':
            title = request.POST['title']
            body = request.POST['body']
            image = request.FILES['image']
            user = User.objects.get(id=request.user.id)
            blog = Blog(user=user, title=title, body=body, image=image)
            blog.save()
            return redirect('blog_ar')
        return render(request, 'addblog-ar.html')


def blogdetails_ar(request,id):
    #single blog 
    id=id
    blog = Blog.objects.get(id=id)
    # comment
    comment = Comment.objects.filter(blog=blog)
    context = {'blog': blog, 'comments': comment}
    if request.method == 'POST':
        comment = request.POST['comment']
        user = User.objects.get(id=request.user.id)
        blog = Blog.objects.get(id=id)
        comment = Comment(user=user, blog=blog, comment=comment)
        comment.save()
        return redirect('blog:blogdetails_ar', id)
    return render(request, 'single-post-ar.html', context)
        
        
        
        
        
        
def contains_arabic(text):
    arabic_pattern = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+') # Matches Arabic Unicode characters
    return arabic_pattern.search(text) is not None

def contains_english(text):
    english_pattern = re.compile(r'[A-Za-z]+') # Matches English letters
    return english_pattern.search(text) is not None