from django.contrib import admin
# import portfolio and category
from .models import Portfolio, Category
# Register your models here.

admin.site.register(Portfolio)
admin.site.register(Category)
