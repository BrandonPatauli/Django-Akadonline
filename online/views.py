from audioop import reverse
from http import client
from multiprocessing import context
from wsgiref import validate
from accounts.models import CustomerUser
from django.shortcuts import render, get_object_or_404,redirect,reverse

from online.models import Article, Product_Homme, Product_enfant, Product_femmes, commander

# Create your views here.

def index(request):
    femmes = Product_femmes.objects.all()
    hommes = Product_Homme.objects.all()
    enfants = Product_enfant.objects.all()
    
    context={
        
        'femmes':femmes,
        'hommes':hommes,
        'enfants':enfants
    }
    
    return render(request, 'online/index.html', context)



def meilleur(request):
    clients = CustomerUser.objects.all()
    f = Product_femmes.objects.all()
    h = Product_Homme.objects.all()
    e = Product_enfant.objects.all()
    com = commander.objects.filter(valide=False)
    
    context={
        'clients':clients,
        'f':f,
        'h':h,
        'e':e,
        'com':com
    }
    
    
    return render(request, 'online/index.html', context)


# def achat(request):
#     user = request.user
#     produits_achetes = commander.objects.filter(utilisateur=user)
    
#     return render(request, 'Online/reservation.html', {'produits_achetes': produits_achetes})


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



    



def product_detail(request, slug):
    producter = get_object_or_404(Product_femmes, slug=slug)
    return render(request, 'reservation/reservation.html', conntext={"producter":producter})


def about(request):
    
    return render(request, 'online/about.html')
