from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomerUser(AbstractUser):
    
    numero_telephone = models.CharField(max_length=15, default=00000000000)