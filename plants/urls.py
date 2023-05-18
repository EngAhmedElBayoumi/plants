from django.urls import path
from . import views
app_name="plants"
urlpatterns = [
    path('plants',views.plants,name="plants"),
    path('plantdetials<int:id>',views.plantdetails,name="plantdetials"),
    path('card<int:id>',views.card,name="card"),
    path('pay',views.pay,name="pay"),
     #ar
    path('plants_ar',views.plants_ar,name="plants_ar"),
    path('plantdetials_ar<int:id>',views.plantdetails_ar,name="plantdetials_ar"),
    path('card_ar<int:id>',views.card_ar,name="card_ar"),
    path('pay_ar',views.pay_ar,name="pay_ar"),             
    
]