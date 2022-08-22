from audioop import reverse
from gc import get_objects
from http import client
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import CustomerUser
from online.models import Article, Product_femmes, commander



# Create your views here.



def reservation(request):
    
    # cart = get_object_or_404(commander, user=request.user)
    # ,context={"articles":cart.articles.all()}
    
    return render(request,'reservation/reservation.html')

def add_to_cart(request):
    user = request.user
    product = get_object_or_404(Product_femmes, slug=slug)
    cart, _ =commander.objects.get_or_create(user=user)
    ordre, created = Article.objects.get_or_create(user=user,
                                                   product=product)
    
    
    
    if created:
        cart.articles.add(ordre)
        cart.save()
        
    else:
        ordre.quantity +=1
        ordre.save()
        
    return redirect(reverse("product", kwrags={"slug":slug}))






