from cProfile import label
from dataclasses import field
from msilib.schema import Class
from pyexpat import model
from tkinter import Widget

from django import forms

from ..online.models import Product
from .models import commentaire

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ('Photo')
        
class ComForm(forms.ModelForm):
    class  Meta:
        model = commentaire
        field = ('corps') 
        label = {'corps':'commentaire'}
        Widget ={
            'corps':forms.Textarea
        }
         
   