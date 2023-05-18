from django.urls import path
from . import views
app_name="portfolio"
urlpatterns = [
    path('portfolio',views.portfolio,name="portfolio"),
    path('portfolio_ar',views.portfolio_ar,name="portfolio_ar")
]