from http import client
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render
from accounts.models import CustomerUser



# Create your views here.

def reservation(request):

    
    return render(request,'reservation/reservation.html')

