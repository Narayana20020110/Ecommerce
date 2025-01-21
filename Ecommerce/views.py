from django.shortcuts import render,redirect
from .models import Product
from .forms import MyForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.files.storage import FileSystemStorage
def register(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            form.save()
            user = form.get_user()
            login(request,user)
            return redirect('products')
    else :
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})
@login_required
def products(request):
    products = Product.objects.all()
    return render(request,'products.html',{
        'products' : products
    })
@login_required
def add(request):
    if request.method == 'POST':
        form = MyForm(request.POST,request.FILES)
        if form.is_valid():
            id = form.cleaned_data['id']
            name = form.cleaned_data['name']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            filename = fs.save(image.name,image)
            image = fs.url(filename)
            price = form.cleaned_data['price']
        product = Product(id,name,image,price)
        product.save()
        return redirect('products')
    else :
        form = MyForm()
    return render(request,'productForm.html',{'form':form})
@login_required
def delete(request,id):
    product = Product.objects.filter(id=id)
    product.delete()
    return redirect('products')
@login_required
def update(request,id):
   if request.method == 'POST':
      form = MyForm(request.POST,request.FILES)
      if form.is_valid():
         name = form.cleaned_data['name']
         image=form.cleaned_data['image']
         fs = FileSystemStorage()
         filename = fs.save(image.name,image)
         file_url = fs.url(filename)
         price = form.cleaned_data['price']
         product = Product(id,name,file_url,price)
         product.save()
         return redirect('products')
   else :
       form = MyForm()
   return render(request,'update.html',{'form':form})