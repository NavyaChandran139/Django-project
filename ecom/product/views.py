from django.shortcuts import render,redirect
from .forms import ProductAddForm
from django.contrib import messages
from .models import ProductDetail

def AddProduct(request):
    form = ProductAddForm()
    if request.method == "POST":
        form = ProductAddForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save()
            product.Merchant = request.user
            product.save()
            messages.info(request,"Product Added To list")
            return redirect('AddProduct')

    return render(request,"admin/addproduct.html",{"form":form})

def ProductViewMerchant(request):
    products = ProductDetail.objects.all()
    context = {
        "products":products
    }

    return render(request,"admin/productlistview.html",context)

def DeleteProduct(request,pk):
    product = ProductDetail.objects.get(Product_Id = pk)
    product.Product_Image.delete()
    product.delete()
    messages.info(request,"Product deleted")
    return redirect("ProductViewMerchant")

def UpdateProduct(request,pk):
    product = ProductDetail.objects.filter(Product_Id = pk)
    if request.method == "POST":

        pname = request.POST['pname']
        pbrand = request.POST["pbrand"]
        pdis = request.POST["pdis"]
        pprice = request.POST["pprice"]
        pstock = request.POST["pstock"]
        image = request.FILES["image"]

        item = ProductDetail.objects.get(Product_Id = pk)

        item.Product_Name = pname
        item.Product_Brand = pbrand
        item.Product_Discription = pdis
        item.Product_Price = pprice
        item.Product_Stock = pstock
        item.Product_Image.delete()
        item.Product_Image = image
        item.save()
        messages.info(request,"Item Updated")
        return redirect("UpdateProduct",pk=pk)

    context = {
         "products":product

    }
    return render(request,"admin/updateproduct.html",context)

def ViewProduct(request,pk):
    product = ProductDetail.objects.filter(Product_Id=pk)
    context = {
         "products":product

    }
    return render(request,"viewproduct.html",context)



