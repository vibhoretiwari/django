from django.shortcuts import render
from django.views import View
from.models import Customer,Product,Cart,OrderPlace


#def home(request):
 #return render(request, 'app/home.html')
def home(request):
    topwear=Product.objects.filter(category='tw')
    bottomwear=Product.objects.filter(category='bw')
    mobile=Product.objects.filter(category='m')
    return render(request,'app/home.html',{'topwear':topwear,'bottomwear': bottomwear,'mobile':mobile})

def product_detail(request):
    return render(request, 'app/productdetail.html')

def add_to_cart(request):
    return render(request, 'app/addtocart.html')

#class ProductDetailView(View):
 #   def get(self,request,pk):
 #       product=Product.objects.get(pk=pk)
  #      return render(request, 'app/productdetail.html',{'product':product})

def buy_now(request):
    return render(request, 'app/buynow.html')

def profile(request):
    return render(request, 'app/profile.html')

def address(request):
    return render(request, 'app/address.html')

def orders(request):
    return render(request, 'app/orders.html')

def change_password(request):
    return render(request, 'app/changepassword.html')

def mobile(request):
    return render(request, 'app/mobile.html')

def login(request):
    return render(request, 'app/login.html')

def customerregistration(request):
    return render(request, 'app/customerregistration.html')

def checkout(request):
    return render(request, 'app/checkout.html')
