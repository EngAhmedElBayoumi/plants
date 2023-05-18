from django.shortcuts import render
from portfolio.models import Portfolio, Category
from blog.models import Blog
from contact.models import Contact
from django.contrib import messages
# Create your views here.

def home(request):
    #get all the categories
    categories = Category.objects.all()
    #get all the portfolios
    portfolios = Portfolio.objects.all()
    #get first 3 blogs
    blogs = Blog.objects.filter(title__regex=r'[A-Za-z]+')[:3]
    #create a dictionary
    context = {'category':categories,'portfolio':portfolios,'blog':blogs}
    # contact 
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, 'تم ارسال الرساله بنجاح')
    return render(request, 'index.html',context)

def home_ar(request):
    #get all the categories
    categories = Category.objects.all()
    #get all the portfolios
    portfolios = Portfolio.objects.all()
    #get first 3 blogs
    blogs = Blog.objects.filter(title__regex=r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+')[:3]
    #create a dictionary
    context = {'category':categories,'portfolio':portfolios,'blog':blogs}
    # contact 
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        messages.success(request, 'تم ارسال الرساله بنجاح')
    return render(request, 'index-ar.html',context)