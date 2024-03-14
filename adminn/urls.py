
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    
    path('adminn/',views.adminn,name='adminn'),
    path('dashboard/',views.adminn_dashboard,name='adminn_dashboard'),
    path('logout/',views.logout,name='logout'),
    path('category/',views.category,name='category'),
    path('add-category/',views.add_category,name="add-category"),
    
    path('update-category/<pk>',views.UpdateCategory,name='update-category'),
    path('products-list',views.product_list,name='product_list'),
    path('add-products',views.add_products,name='add_products')
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)