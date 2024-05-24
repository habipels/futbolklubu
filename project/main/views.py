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
    sozluk ["hakkimizda"] = hakkimizda.objects.last()
    sozluk["teknik_kadro_ekibi"] = teknik_kadro_ekibi.objects.all()
    sozluk["site_adi"] = site_adi.objects.last()
    sozluk["numara"] = numara.objects.last()
    sozluk["adres"] = adres.objects.last()
    sozluk["email_adres"] = email_adres.objects.last()
    sozluk["sosyalmedyaInsgr"] = sosyalmedyaInsgr.objects.last()
    sozluk["sosyalmedyalinkd"] = sosyalmedyalinkd.objects.last()
    sozluk["sosyalmedyaFace"] = sosyalmedyaFace.objects.last()
    sozluk["sosyalmedyayoutube"] = sosyalmedyayoutube.objects.last()
    sozluk["sosyalmedyatw"] = sosyalmedyatw.objects.last()
    sozluk["seo_ayarlari"] = seo_ayarlari.objects.last()
    
    return sozluk
# Create your views here.
def homepage(request):
    content = site_bilgileri_cek()
    return render(request,"index.html",content)

def about(request):
    content = site_bilgileri_cek()
    return render(request,"about.html",content)
def teknik_kadromuz(request):
    content = site_bilgileri_cek()
    return render(request,"teknik_kadromuz.html",content)

def fotograflar(request):
    content = site_bilgileri_cek()
    content["foto"] = formalarimiz.objects.order_by("-id")
    return render(request,"galery.html",content)
def u_11(request):
    content = site_bilgileri_cek()
    content["foto"] = u_11_fotograflari.objects.order_by("-id")
    return render(request,"galery.html",content)
def u_12(request):
    content = site_bilgileri_cek()
    content["foto"] = u_12_fotograflari.objects.order_by("-id")
    return render(request,"galery.html",content)
def u_13(request):
    content = site_bilgileri_cek()
    content["foto"] = u_13_fotograflari.objects.order_by("-id")
    return render(request,"galery.html",content)

def u_11_oyuncularimiz(request):
    content = site_bilgileri_cek()
    content["foto"] = u_11_oyunculari.objects.order_by("-id")
    content["u11"] = "U-11 Oyuncularımız"
    return render(request,"oyuncular.html",content)
def u_12_oyuncularimiz(request):
    content = site_bilgileri_cek()
    content["foto"] = u_12_oyunculari.objects.order_by("-id")
    content["u11"] = "U-12 Oyuncularımız"
    return render(request,"oyuncular.html",content)
def u_13_oyuncularimiz(request):
    content = site_bilgileri_cek()
    content["foto"] = u_13_oyunculari.objects.order_by("-id")
    content["u11"] = "U-13 Oyuncularımız"
    return render(request,"oyuncular.html",content)
def iletisim(request):
    content = site_bilgileri_cek()
    return render(request,"iletisim.html",content)