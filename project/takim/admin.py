from django.contrib import admin
from django.utils.html import mark_safe
from .models import *
from django.contrib.admin import AdminSite

class ImageAdminMixin:
    def image_tag(self, obj):
        if obj.fotografi:
            return mark_safe(f'<img src="{obj.fotografi.url}" width="50" height="50" />')
        return "-"
    image_tag.short_description = 'Image'

    def file_tag(self, obj):
        if obj.ev_sahibi_takim_logusu or obj.deplasman_takim_logusu:
            ev_sahibi_logo = f'<img src="{obj.ev_sahibi_takim_logusu}" width="50" height="50" />' if obj.ev_sahibi_takim_logusu else "-"
            deplasman_logo = f'<img src="{obj.deplasman_takim_logusu}" width="50" height="50" />' if obj.deplasman_takim_logusu else "-"
            return mark_safe(f'Ev Sahibi: {ev_sahibi_logo}<br>Deplasman: {deplasman_logo}')
        return "-"
    file_tag.short_description = 'Logos'

@admin.register(u_11_takimi_son_karsilasma)
class u_11_takimi_son_karsilasmaAdmin(admin.ModelAdmin, ImageAdminMixin):
    list_display = ('ev_sahibi_takim_adi', 'deplasman_takim_adi', 'karsilasma_tarihi', 'file_tag')
    search_fields = ('ev_sahibi_takim_adi', 'deplasman_takim_adi', 'karsilasma_tarihi')

@admin.register(u_12_takimi_son_karsilasma)
class u_12_takimi_son_karsilasmaAdmin(admin.ModelAdmin, ImageAdminMixin):
    list_display = ('ev_sahibi_takim_adi', 'deplasman_takim_adi', 'karsilasma_tarihi', 'file_tag')
    search_fields = ('ev_sahibi_takim_adi', 'deplasman_takim_adi', 'karsilasma_tarihi')

@admin.register(u_13_takimi_son_karsilasma)
class u_13_takimi_son_karsilasmaAdmin(admin.ModelAdmin, ImageAdminMixin):
    list_display = ('ev_sahibi_takim_adi', 'deplasman_takim_adi', 'karsilasma_tarihi', 'file_tag')
    search_fields = ('ev_sahibi_takim_adi', 'deplasman_takim_adi', 'karsilasma_tarihi')

@admin.register(u_11_skor_sayfasi)
class u_11_skor_sayfasiAdmin(admin.ModelAdmin):
    list_display = ('url_bilgisi',)
    search_fields = ('url_bilgisi',)

@admin.register(u_12_skor_sayfasi)
class u_12_skor_sayfasiAdmin(admin.ModelAdmin):
    list_display = ('url_bilgisi',)
    search_fields = ('url_bilgisi',)

@admin.register(u_13_skor_sayfasi)
class u_13_skor_sayfasiAdmin(admin.ModelAdmin):
    list_display = ('url_bilgisi',)
    search_fields = ('url_bilgisi',)

@admin.register(teknik_kadro_ekibi)
class teknik_kadro_ekibiAdmin(admin.ModelAdmin, ImageAdminMixin):
    list_display = ('adi_soyadi', 'dogum_tarihi', 'gorevi', 'image_tag')
    search_fields = ('adi_soyadi', 'dogum_tarihi', 'gorevi')

@admin.register(formalarimiz)
class formalarimizAdmin(admin.ModelAdmin, ImageAdminMixin):
    list_display = ('baslik', 'aciklamasi', 'image_tag')
    search_fields = ('baslik', 'aciklamasi')

@admin.register(u_11_fotograflari)
class u_11_fotograflariAdmin(admin.ModelAdmin, ImageAdminMixin):
    list_display = ('baslik', 'aciklamasi', 'image_tag')
    search_fields = ('baslik', 'aciklamasi')

@admin.register(u_12_fotograflari)
class u_12_fotograflariAdmin(admin.ModelAdmin, ImageAdminMixin):
    list_display = ('baslik', 'aciklamasi', 'image_tag')
    search_fields = ('baslik', 'aciklamasi')

@admin.register(u_13_fotograflari)
class u_13_fotograflariAdmin(admin.ModelAdmin, ImageAdminMixin):
    list_display = ('baslik', 'aciklamasi', 'image_tag')
    search_fields = ('baslik', 'aciklamasi')

@admin.register(u_11_oyunculari)
class u_11_oyunculariAdmin(admin.ModelAdmin, ImageAdminMixin):
    list_display = ('adi_soyadi', 'forma_numarasi', 'boyu', 'kilosu', 'dogum_tarihi', 'mevki', 'hobisi', 'aciklamasi', 'image_tag')
    search_fields = ('adi_soyadi', 'forma_numarasi', 'mevki')

@admin.register(u_12_oyunculari)
class u_12_oyunculariAdmin(admin.ModelAdmin, ImageAdminMixin):
    list_display = ('adi_soyadi', 'forma_numarasi', 'boyu', 'kilosu', 'dogum_tarihi', 'mevki', 'hobisi', 'aciklamasi', 'image_tag')
    search_fields = ('adi_soyadi', 'forma_numarasi', 'mevki')

@admin.register(u_13_oyunculari)
class u_13_oyunculariAdmin(admin.ModelAdmin, ImageAdminMixin):
    list_display = ('adi_soyadi', 'forma_numarasi', 'boyu', 'kilosu', 'dogum_tarihi', 'mevki', 'hobisi', 'aciklamasi', 'image_tag')
    search_fields = ('adi_soyadi', 'forma_numarasi', 'mevki')


@admin.register(sponsorlar)
class sponsorlarimiz(admin.ModelAdmin, ImageAdminMixin):
    list_display = ('adi_soyadi', 'image_tag')
    search_fields = ('adi_soyadi',)