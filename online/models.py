from audioop import reverse
from distutils.command.upload import upload
from itertools import product
from unicodedata import name
from django.db import models

from Shop.settings import AUTH_USER_MODEL


# Create your models here.
class Product(models.Model):
    
    name_product = models.CharField(max_length=120)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='products',blank=True, null=True)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('product', kwargs={"slug":self.slug})
    
    

        
# gestion de l'ordre du pagner utilisateur, produit, quantiter, commander ou non 

class Article(models.Model):
     user = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)
     product = models.ForeignKey(Product, on_delete=models.CASCADE)
     quantity = models.IntegerField(default=1)
     commande =  models.BooleanField(default=False)
    
     def __str__(self):
         return f"{self.product.name} ({self.quantity})"
    
# gestion de carte nous Utilisateur, article, commander ou non, date de la commande


class commander(models.Model):
     user = models.OneToOneField(AUTH_USER_MODEL,on_delete=models.CASCADE)
     articles =models.ManyToManyField(Article)
     commande = models.BooleanField(default=False)
     date_commande = models.DateTimeField(blank=True, null=True)
    
     def __str__(self):
         return self.user.username
    