from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Profil.views import profil
from online.views import about, add_to_cart, index,product_detail
from accounts.views import  logout_user, signup, signin
from Shop import settings
from reservation.views import reservation
urlpatterns = [
    path('',index, name="index"),
    path('reservation/',reservation, name="reservation"),
    path('Profil/',profil, name="profil"),
    path('about/',about, name="about"),
    path('logout/',logout_user, name="logout_user"),
    path('signup/',signup, name="signup"),
    path('signin/',signin, name="signin"),
    path('admin/', admin.site.urls),
    path('product/<str:slug>/',product_detail, name="product"),
    path('product/<str:slug>/add_to_cart',add_to_cart, name="add_to_cart"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
