from django.urls import path
from . import views

app_name="about"
urlpatterns = [
    path('about',views.about,name="about"),
    path('about_ar',views.about_ar,name="about_ar")
]