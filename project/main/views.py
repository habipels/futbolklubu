from django.shortcuts import render
from django.http import HttpResponse
from site_settings.models import *
from takim.models import *
def site_bilgileri_cek():
    sozluk = {}
    sozluk["site_adi"] = site_adi.objects.last()
    sozluk["logo"] =sayfa_logosu.objects.last()
    sozluk["favicon"] = sayfa_iconu.objects.last()
    sozluk["u_11_sonkarsilasma"] = u_11_takimi_son_karsilasma.objects.last()
    sozluk["u_12_sonkarsilasma"] = u_12_takimi_son_karsilasma.objects.last()
    sozluk["u_13_sonkarsilasma"] = u_13_takimi_son_karsilasma.objects.last()
    return sozluk
# Create your views here.
def homepage(request):
    content = site_bilgileri_cek()
    return render(request,"index.html",content)