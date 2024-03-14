
from django.urls import path,include
from . import views


urlpatterns = [
   
    path('',views.index,name='home'),
    path('product-detail',views.product_detail_page,name='product-detail')
    
]