from django.shortcuts import render
#import portfolio and category
from .models import Portfolio, Category


# Create your views here.

def portfolio(request):
    #get all the categories
    categories = Category.objects.all()
    #get all the portfolios
    portfolios = Portfolio.objects.all()
    #create a dictionary
    context = {'category':categories,'portfolio':portfolios}
    return render(request,'portfolio.html',context)

#ar
def portfolio_ar(request):
    #get all the categories
    categories = Category.objects.all()
    #get all the portfolios
    portfolios = Portfolio.objects.all()
    #create a dictionary
    context = {'category':categories,'portfolio':portfolios}
    return render(request,'portfolio-ar.html',context)