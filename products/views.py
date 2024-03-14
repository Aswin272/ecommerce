from django.shortcuts import render
from .models import Category,Product


# Create your views here.

def index(request):
    category=Category.objects.filter(is_active=True)
    products=Product.objects.filter(is_active=True)
    return render(request,'index.html',{'category':category,'products':products})


def product_detail_page(request):
    return render(request,'product_detail_page.html')











# def product_list(request):
#     if request.method =='POST':
#         product_form=ProductForm(request.POST,request.FILES)
#         product_img=ProductImageForm(request.POST,request.FILES)

#         if product_form.is_valid():
#             product=product_form.save()
#             product_id=product.id
            
#             images=request.FILES.getlist('image')
#             for img in images:
#                 ProductImage.objects.create(product_id=product_id,image=img)
                
#         else:
#             print('forms are not valid',product_form.errors,product_img.errors)
#     else:
#         product_form=ProductForm()
        
#     return render(request,'admin_product.html',{'frm':product_form})