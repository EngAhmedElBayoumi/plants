from django.urls import path
from . import views
app_name="blog"
urlpatterns = [
    path('blog',views.blog,name="blog"),
    path('blogdetails<int:id>',views.blogdetails,name="blogdetails"),
    path('addblog',views.addblog,name="addblog"),
    #ar
    path('blog_ar',views.blog_ar,name="blog_ar"),
    path('blogdetails_ar<int:id>',views.blogdetails_ar,name="blogdetails_ar"),
    path('addblog_ar',views.addblog_ar,name="addblog_ar"),
    
]