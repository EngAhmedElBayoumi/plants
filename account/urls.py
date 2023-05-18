from django.urls import path
from . import views
app_name="account"
urlpatterns = [
    path('login',views.log_in,name="login"),
    path('logout',views.log_out,name="logout"),
    path('signin',views.sign_in,name="signin"),
    #ar
    path('login_ar',views.log_in_ar,name="login_ar"),
    path('logout_ar',views.log_out_ar,name="logout_ar"),
    path('signin_ar',views.sign_in_ar,name="signin_ar"),
]