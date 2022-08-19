from django.contrib import admin

# Register your models here.
from online.models import Article, Product, commander
 
 
 
admin.site.register(Product)
admin.site.register(Article)
admin.site.register(commander)

