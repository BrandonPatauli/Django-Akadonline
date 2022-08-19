import numbers
from unicodedata import name
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.shortcuts import redirect, render
from accounts.models import CustomerUser
from django.http import HttpResponse

# Create your views here.

User = get_user_model()

def signup(request):
    
    if request.method == 'POST':
        
        nom = request.POST.get('nom')
        username = request.POST.get('username')
        password = request.POST.get('password')
        telephone = request.POST.get('telephone')
        
        
        user = User.objects.create_user(username=username,
                                        first_name=nom,
                                        password=password,
                                        numero_telephone=telephone)
        login(request, user)
        return redirect('index')
        
    return render(request, "accounts/signup.html")

    
def signin(request):
    if request.method =='POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username,
                            password=password)
        if user:
            login(request, user)
            return redirect('index')
      
    return render(request, "accounts/signin.html")     

def logout_user(request):
    
    logout(request)
    
    return redirect('index')