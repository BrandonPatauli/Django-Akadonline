from django.contrib import admin

# Register your models here.
from online.models import Article, Product_Homme, Product_enfant, Product_femmes, commander
 
 
 
admin.site.register(Product_femmes)
admin.site.register(Product_Homme)
admin.site.register(Product_enfant)
admin.site.register(Article)
admin.site.register(commander)

