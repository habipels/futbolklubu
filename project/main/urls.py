from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("sportsschool", views.spor_okuluu, name="spor_okuluu"),
    path("fixture", views.fikstur, name="fikstur"),
    path("about", views.about, name="about"),
    path("galery", views.fotograflar, name="fotograflar"),
    path("u11galery", views.u_11, name="u_11"),
    path("u12galery", views.u_12, name="u_12"),
    path("u13galery", views.u_13, name="u_13"),
    path("ourtechnicalstaff", views.teknik_kadromuz, name="teknik_kadromuz"),
    path("u11player", views.u_11_oyuncularimiz, name="u_11_oyuncularimiz"),
    path("u12player", views.u_12_oyuncularimiz, name="u_12_oyuncularimiz"),
    path("u13player", views.u_13_oyuncularimiz, name="u_13_oyuncularimiz"),
    path("contact", views.iletisim, name="iletisim"),
    path("manager", views.yonetim_ekibi, name="yonetim_ekibi"),
    path("awards", views.kupalar, name="kupalar"),
    path("sponsors", views.sponsorluklar, name="sponsorluklar"),
    path("contactsave", views.iletisim_kaydet, name="iletisim_kaydet"),
]#