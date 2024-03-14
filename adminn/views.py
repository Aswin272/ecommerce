from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.views.decorators.cache import never_cache
from products.models import Category,Product,ProductImage
from . forms import UpdateCategoryForm,ProductForm,ProductImageForm
# Create your views here.

@never_cache
def adminn(request):
    if 'superuser' in request.session:
        return redirect('adminn_dashboard')
    
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            request.session['superuser']=username
            return render(request,'admin_dashboard.html')      
            
        
    return render(request,'adminn_signin.html')
@never_cache
def adminn_dashboard(request):
    if 'superuser' in request.session:
        return render(request,'admin_dashboard.html')
    return redirect('adminn')

@never_cache
def logout(request):
    if 'superuser' in request.session:
        request.session.flush()
        
        return redirect('adminn')


# categoryyy----------------------------------------#

@never_cache
def category(request):
    if 'superuser' in request.session:
        
        category_instance=Category.objects.all()
        return render(request,'admin_category.html',{'categories':category_instance})
@never_cache
def add_category(request):
    
    if request.method=='POST':
        categ=request.POST.get('name')
        description=request.POST.get('description')
        Category.objects.create(name=categ,description=description)
        return redirect('category')
    return render(request,'add_category.html')
@never_cache
def UpdateCategory(request,pk):
    if 'superuser' in request.session:
        instance=Category.objects.get(id=pk)
      
        f=UpdateCategoryForm(instance=instance)
        if request.POST:
            fm=UpdateCategoryForm(request.POST,instance=instance)
            
            if fm.is_valid():
                fm.save()
                return redirect('category')
            else:
                f=UpdateCategoryForm(instance=instance)
                
        return render(request,'admin_update_category.html',{'instance':instance,'f':f})
    return redirect('adminn')



#product--------------------------------------

def product_list(request):
    products=Product.objects.all()
    return render(request,'admin_product_list.html',{'products':products})











def add_products(request):
    if request.method =='POST':
        product_form=ProductForm(request.POST,request.FILES)
        product_img=ProductImageForm(request.POST,request.FILES)

        if product_form.is_valid():
            product=product_form.save()
            product_id=product.id
            
            images=request.FILES.getlist('image')
            for img in images:
                ProductImage.objects.create(product_id=product_id,image=img)
                
        else:
            print('forms are not valid',product_form.errors,product_img.errors)
    else:
        product_form=ProductForm()
        
    return render(request,'admin_add_product.html',{'frm':product_form})