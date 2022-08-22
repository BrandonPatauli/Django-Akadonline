from http import client
from django.shortcuts import render

from accounts.models import CustomerUser

from online.models import commander

# Create your views here.

def profil(request):
    
    clients = CustomerUser.objects.all()
    
    command = commander.objects.filter()
    
    
    context={
        'command':command,
        'clients':clients
        
    }
    
    
    
    return render(request, 'Profil/index.html', context)
