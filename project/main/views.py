from django.shortcuts import render,redirect
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
    sozluk["u_14_sonkarsilasma"] = u_14_takimi_son_karsilasma.objects.last()
    sozluk["u_15_sonkarsilasma"] = u_15_takimi_son_karsilasma.objects.last()
    sozluk ["hakkimizda"] = hakkimizda.objects.last()
    sozluk ["anasayfa"] = anasayfa.objects.last()
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
    sozluk["gomuluadres"] = gomulu_adres.objects.last()
    sozluk["renkler"] = site_renkleri.objects.last()
    sozluk["sponsorlar"] = sponsorlar.objects.all()
    sozluk["spor_okulu"] = spor_okulu.objects.last()
    sozluk["teknik_kadro_ekibii"] = yonetim_klubu_ekibi.objects.all()
    sozluk["kupalar"] = kupalarimiz.objects.all()
    
    return sozluk
def page_not_found_view(request, exception):
    content = site_bilgileri_cek()
    if deactive.objects.last().deactive_active:
        return redirect("/error")
    return render(request, '404.html',content)
# Create your views here.
def homepage(request):
    if deactive.objects.last().deactive_active:
        return redirect("/error")
    content = site_bilgileri_cek()
    return render(request,"index.html",content)
def fikstur(request):
    if deactive.objects.last().deactive_active:
        return redirect("/error")
    content = site_bilgileri_cek()
    return render(request,"fikstur.html",content)
def spor_okuluu(request):
    if deactive.objects.last().deactive_active:
        return redirect("/error")
    content = site_bilgileri_cek()
    return render(request,"sporokulu.html",content)
def about(request):
    if deactive.objects.last().deactive_active:
        return redirect("/error")
    content = site_bilgileri_cek()
    return render(request,"about.html",content)
def teknik_kadromuz(request):
    if deactive.objects.last().deactive_active:
        return redirect("/error")
    content = site_bilgileri_cek()
    return render(request,"teknik_kadromuz.html",content)

def fotograflar(request):
    if deactive.objects.last().deactive_active:
        return redirect("/error")
    content = site_bilgileri_cek()
    content["foto"] = formalarimiz.objects.order_by("-id")
    return render(request,"galery.html",content)
def u_11(request):
    if deactive.objects.last().deactive_active:
        return redirect("/error")
    content = site_bilgileri_cek()
    content["foto"] = u_11_fotograflari.objects.order_by("-id")
    return render(request,"galery.html",content)
def u_12(request):
    if deactive.objects.last().deactive_active:
        return redirect("/error")
    content = site_bilgileri_cek()
    content["foto"] = u_12_fotograflari.objects.order_by("-id")
    return render(request,"galery.html",content)
def u_13(request):
    if deactive.objects.last().deactive_active:
        return redirect("/error")
    content = site_bilgileri_cek()
    content["foto"] = u_13_fotograflari.objects.order_by("-id")
    return render(request,"galery.html",content)
def u_14(request):
    if deactive.objects.last().deactive_active:
        return redirect("/error")
    content = site_bilgileri_cek()
    content["foto"] = u_14_fotograflari.objects.order_by("-id")
    return render(request,"galery.html",content)
def u_15(request):
    if deactive.objects.last().deactive_active:
        return redirect("/error")
    content = site_bilgileri_cek()
    content["foto"] = u_15_fotograflari.objects.order_by("-id")
    return render(request,"galery.html",content)
def u_11_oyuncularimiz(request):
    if deactive.objects.last().deactive_active:
        return redirect("/error")
    content = site_bilgileri_cek()
    content["foto"] = u_11_oyunculari.objects.order_by("-id")
    content["u11"] = "U-11 Oyuncularımız"
    return render(request,"oyuncular.html",content)
def u_12_oyuncularimiz(request):
    if deactive.objects.last().deactive_active:
        return redirect("/error")
    content = site_bilgileri_cek()
    content["foto"] = u_12_oyunculari.objects.order_by("-id")
    content["u11"] = "U-12 Oyuncularımız"
    return render(request,"oyuncular.html",content)
def u_13_oyuncularimiz(request):
    if deactive.objects.last().deactive_active:
        return redirect("/error")
    content = site_bilgileri_cek()
    content["foto"] = u_13_oyunculari.objects.order_by("-id")
    content["u11"] = "U-13 Oyuncularımız"
    return render(request,"oyuncular.html",content)
def u_14_oyuncularimiz(request):
    if deactive.objects.last().deactive_active:
        return redirect("/error")
    content = site_bilgileri_cek()
    content["foto"] = u_14_oyunculari.objects.order_by("-id")
    content["u11"] = "U-14 Oyuncularımız"
    return render(request,"oyuncular.html",content)
def u_15_oyuncularimiz(request):
    if deactive.objects.last().deactive_active:
        return redirect("/error")
    content = site_bilgileri_cek()
    content["foto"] = u_15_oyunculari.objects.order_by("-id")
    content["u11"] = "U-15 Oyuncularımız"
    return render(request,"oyuncular.html",content)
def iletisim(request):
    if deactive.objects.last().deactive_active:
        return redirect("/error")
    content = site_bilgileri_cek()
    return render(request,"iletisim.html",content)
def iletisim_kaydet(request):
    if deactive.objects.last().deactive_active:
        return redirect("/error")
    if request.POST:
        isim = request.POST.get("name")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        email = request.POST.get("email")
        comment = request.POST.get("comment")
        iletisim_al.objects.create(adi_soyadi =isim,numara = phone,konu = subject,mesaj = comment,email = email)
    return redirect("/")

def kupalar(request):
    if deactive.objects.last().deactive_active:
        return redirect("/error")
    content = site_bilgileri_cek()
    return render(request,"kupalar.html",content)
def yonetim_ekibi(request):
    if deactive.objects.last().deactive_active:
        return redirect("/error")
    content = site_bilgileri_cek()
    return render(request,"yonetim.html",content)
def sponsorluklar(request):
    if deactive.objects.last().deactive_active:
        return redirect("/error")
    content = site_bilgileri_cek()
    return render(request,"sponsorluk.html",content)

def active_active(request):
    
    deactive.objects.create(deactive_active = False)
    return redirect("/")
def deactive_active(request):
    deactive.objects.create(deactive_active = True)
    return redirect("/")
def page_notfound(request):
    return render(request,"page_isi.html")