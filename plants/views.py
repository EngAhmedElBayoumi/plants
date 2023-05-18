from django.shortcuts import render
from .models import Plants
# import paginator
from django.core.paginator import Paginator

# Create your views here.

def plants(request):
    #get all the categories
    plants = Plants.objects.filter(title__regex=r'[A-Za-z]+')
    #paginator
    paginator = Paginator(plants, 8) # Show 8 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #create a dictionary
    context = {'plants':page_obj}
    return render(request,'plants.html',context)

def plantdetails(request,id):
    #single plant
    plant = Plants.objects.get(id=id)
    context = {'plant':plant}
    return render(request,'plantsdetails.html',context)

def card(request,id):
    #single plant
    plant = Plants.objects.get(id=id)
    context = {'plant':plant}
    return render(request,'cart.html',context)


def pay(request):
    #get id from url query string
    id = request.GET['id']
    #get count from query string in url
    count = request.GET['count']
    #get plant
    plant = Plants.objects.get(id=id)
    #get total price
    total = plant.price * int(count)
    #create a dictionary
    context = {'plant':plant,'count':count,'total':total}
    return render(request,'checkout.html',context)


#ar

def plants_ar(request):
    #get all the categories
    plants = Plants.objects.filter(title__regex=r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+')
    #paginator
    paginator = Paginator(plants, 8) # Show 8 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #create a dictionary
    context = {'plants':page_obj}
    return render(request,'plants-ar.html',context)


def plantdetails_ar(request,id):
    #single plant
    plant = Plants.objects.get(id=id)
    context = {'plant':plant}
    return render(request,'plantsdetails-ar.html',context)

def card_ar(request,id):
    #single plant
    plant = Plants.objects.get(id=id)
    context = {'plant':plant}
    return render(request,'cart-ar.html',context)


def pay_ar(request):
    #get id from url query string
    id = request.GET['id']
    #get count from query string in url
    count = request.GET['count']
    #get plant
    plant = Plants.objects.get(id=id)
    #get total price
    total = plant.price * int(count)
    #create a dictionary
    context = {'plant':plant,'count':count,'total':total}
    return render(request,'checkout-ar.html',context)