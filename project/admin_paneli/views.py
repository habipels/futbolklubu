from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .decorators import user_not_authenticated
from .tokens import account_activation_token
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@user_not_authenticated
def admin_login(request):
    if request.POST:
        kullanici_adi = request.POST.get("username")
        sifre = request.POST.get("sifre")
        user = authenticate(username = kullanici_adi,password = sifre)
        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return redirect("/yonetim/girisyap/")
        login(request,user)
        return redirect("/")
    return render(request,"adminlogin.html")