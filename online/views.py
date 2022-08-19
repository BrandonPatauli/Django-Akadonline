from multiprocessing import context
from django.shortcuts import render, get_object_or_404

from online.models import Product
# from online.models import Product_enfant, Product_homme, Product_femme
# Create your views here.

def index(request):
     product = Product.objects.all()
    
    
     return render(request, 'online/index.html', context={"product":product})



def product_detail(request, slug):
    producter = get_object_or_404(Product, slug=slug)
    return render(request, 'online/reservation.html', conntext={"producter":producter})


def about(request):
    
    return render(request, 'online/about.html')
