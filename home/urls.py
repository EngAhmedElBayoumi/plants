from django.urls import path
from . import views
app_name="home"
urlpatterns = [
    path('',views.home,name="home"),
    path('home_ar',views.home_ar,name="home_ar"),
]