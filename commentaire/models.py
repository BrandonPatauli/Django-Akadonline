from django.db import models

from Shop.settings import AUTH_USER_MODEL
from online.models import Product_femmes

# Create your models here.


class commentaire(models.Model):
    Produit = models.ForeignKey(Product_femmes, null=True, on_delete=models.CASCADE, related_name='Comments')
    nom_comment = models.CharField(max_length=125, blank=True)
    #reponse = models.ForeignKey(commentaire, null=True, blank=True, on_delete=models.CASCADE, related_name='reply')
    auteur = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,)
    corps =models.TextField(max_length=200,)
    date_add = models.DateTimeField(auto_now_add=True)
    
    
    def save(self, *args, **kwargs):
        self.nom_comment= slugfy("commenter par:" +str(self.auteur )+ "a"+str(self.date_add))
        
        super.save(*args, **kwargs)
        
        def __str__(self):
            return self.nom_comment
        
        
class Meta:
    ordering = ['-date_add']
    
            
