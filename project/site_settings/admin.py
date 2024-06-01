from django.contrib import admin
from django.utils.html import mark_safe
# Register your models here.
from .models import * 
from django.apps import AppConfig



class ImageAdminMixin:
    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return "-"
    image_tag.short_description = 'Image'
    def file_tag(self, obj):
        if obj.sayfa_icon:
            return mark_safe(f'<img src="{obj.sayfa_icon.url}" width="50" height="50" />')
        return "-"
    file_tag.short_description = 'Icon'
@admin.register(sayfa_logosu)
class SayfaLogosuAdmin(admin.ModelAdmin,ImageAdminMixin):
    list_display = ('image_tag',)

@admin.register(sayfa_iconu)
class SayfaIconuAdmin(admin.ModelAdmin,ImageAdminMixin):
    list_display = ('file_tag',)

@admin.register(site_adi)
class SiteAdiAdmin(admin.ModelAdmin):
    list_display = ('site_adi_genel', 'site_adi_sekme_tr', 'site_kelimeleri')

@admin.register(numara)
class NumaraAdmin(admin.ModelAdmin):
    list_display = ('sirket_numarasi_gosterilecek_metin', 'sirket_numarasi')

@admin.register(adres)
class AdresAdmin(admin.ModelAdmin):
    list_display = ('sirket_adresi_tr',)

@admin.register(gomulu_adres)
class GomuluAdresAdmin(admin.ModelAdmin):
    list_display = ('sirket_adresi_tr',)

@admin.register(email_adres)
class EmailAdresAdmin(admin.ModelAdmin):
    list_display = ('sirket_email_adresi',)

@admin.register(sosyalmedyaInsgr)
class SosyalMedyaInstagramAdmin(admin.ModelAdmin):
    list_display = ('link',)

@admin.register(sosyalmedyalinkd)
class SosyalMedyaLinkedinAdmin(admin.ModelAdmin):
    list_display = ('link',)

@admin.register(sosyalmedyaFace)
class SosyalMedyaFacebookAdmin(admin.ModelAdmin):
    list_display = ('link',)

@admin.register(sosyalmedyayoutube)
class SosyalMedyaYoutubeAdmin(admin.ModelAdmin):
    list_display = ('link',)

@admin.register(sosyalmedyatw)
class SosyalMedyaTwitterAdmin(admin.ModelAdmin):
    list_display = ('link',)

@admin.register(seo_ayarlari)
class SeoAyarlarıAdmin(admin.ModelAdmin):
    list_display = ('site_seo_kelimeleri_tr', 'site_seo_metni_tr')

@admin.register(banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('banner_basligi_tr', 'banner_aciklama_tr', 'banner_sira', 'banner_gosterme', 'banner_link', 'image')

@admin.register(hakkimizda)
class HakkimizdaAdmin(admin.ModelAdmin):
    list_display = ('hakkimizda_tr',)

@admin.register(anasayfa)
class AnasayfaAdmin(admin.ModelAdmin):
    list_display = ('hakkimizda_tr',)

@admin.register(site_renkleri)
class RenklerAdmin(admin.ModelAdmin):
    
    list_display = ["renkbir", "renkbir_goster", "renkiki", "renkiki_goster", "renkuc", "renkuc_goster", "renkdort", "renkdort_goster"]