from django.db import models
# Create your models here.
# Create your models here.
from PIL import Image
from io import BytesIO
class sayfa_logosu(models.Model):
    image  = models.ImageField(upload_to='logo/',verbose_name="Sayfaya Logo Ekleyin")
    def save(self, *args, **kwargs):
        super(sayfa_logosu, self).save(*args, **kwargs)
        if self.image:
            with Image.open(self.image.path) as img:
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                width, height = img.size
                if width > 800:
                    new_width = 800
                    new_height = int((new_width / width) * height)
                    img = img.resize((new_width, new_height), Image.ANTIALIAS)
                    buffer = BytesIO()
                    img.save(buffer, format='JPEG', quality=60)
                    self.image.save(self.image.name, content=buffer, save=False)
                    super(sayfa_logosu, self).save(*args, **kwargs)
    class Meta:
        verbose_name = "Sayfa Logosu"
        verbose_name_plural = "Sayfa Logoları"
class sayfa_iconu(models.Model):
    sayfa_icon = models.FileField(upload_to='logo/',verbose_name="Sayfaya ikon ekleyin")
    class Meta:
        verbose_name = "Sayfa İconu"
        verbose_name_plural = "Sayfa İconları"
class site_adi(models.Model):
    site_adi_genel = models.CharField(max_length=200,verbose_name="Google Nasıl Görünecek")
    site_adi_sekme_tr= models.CharField(max_length=200,verbose_name="Sekmede Görünme Türkçe")
    site_kelimeleri = models.CharField(max_length=200,verbose_name="Seo Kelşmeleri")
    def __str__(self):
        return self.site_adi_genel
    class Meta:
        verbose_name = "Sayfa Adı"
        verbose_name_plural = "Sayfa Adları"

class numara(models.Model):
    sirket_numarasi_gosterilecek_metin = models.CharField(max_length=20,verbose_name="Telefon Sitede Nasıl görünecek" )
    sirket_numarasi = models.CharField(max_length=20,verbose_name="Aranacak Numara Başında + olmadan ülke kodu ile Yazabilirisniz")
    def __str__(self):
        return self.sirket_numarasi_gosterilecek_metin
    class Meta:
        verbose_name = "Şirket Numarası"
        verbose_name_plural = "Şirket Numaraları"

class adres(models.Model):
    sirket_adresi_tr = models.CharField(max_length=200,verbose_name="Şirket Adresi Türkçe")
    def __str__(self):
        return self.sirket_adresi_tr
    class Meta:
        verbose_name = "Şirket Adresi Yazı Olarak"
        verbose_name_plural = "Şirket Adresi Yazı Olarak"
class gomulu_adres(models.Model):
    sirket_adresi_tr = models.CharField(max_length=1000,verbose_name="Şirket Adresi Türkçe")
    def __str__(self):
        return self.sirket_adresi_tr
    class Meta:
        verbose_name = "Şirket Adresi Harita Gömme"
        verbose_name_plural = "Şirket Adresi Harita Gömme"
class email_adres(models.Model):
    sirket_email_adresi = models.EmailField(max_length=200,verbose_name="Şirket Email Adresi")
    def __str__(self):
        return self.sirket_email_adresi
    class Meta:
        verbose_name = "Şirket Email Adresi "
        verbose_name_plural = "Şirket Email Adresi"

class sosyalmedyaInsgr(models.Model):
    link = models.CharField(max_length=400,verbose_name="Şirket İnstagram Linki")
    class Meta:
        verbose_name = "Şirket İnstagram Adresi "
        verbose_name_plural = "Şirket İnstagram Adresi"
class sosyalmedyalinkd(models.Model):
    link = models.CharField(max_length=400,verbose_name="Şirket Linkedin Linki")
    class Meta:
        verbose_name = "Şirket Linkedin Adresi "
        verbose_name_plural = "Şirket Linkedin Adresi"
class sosyalmedyaFace(models.Model):
    link = models.CharField(max_length=400,verbose_name="Şirket Facebook Linki")
    class Meta:
        verbose_name = "Şirket Facebook Adresi "
        verbose_name_plural = "Facebook Linkedin Adresi"
class sosyalmedyayoutube(models.Model):
    link = models.CharField(max_length=400,verbose_name="Şirket Youtube Linki")
    class Meta:
        verbose_name = "Şirket Youtube Adresi "
        verbose_name_plural = "Facebook Youtube Adresi"
class sosyalmedyatw(models.Model):
    link = models.CharField(max_length=400,verbose_name="Şirket TW Linki")
    class Meta:
        verbose_name = "Şirket Twitter Adresi "
        verbose_name_plural = "Facebook Twitter Adresi"
class seo_ayarlari(models.Model):
    site_seo_kelimeleri_tr =models.TextField(max_length=400,verbose_name="Seo Kelmeleri Türkçe")
    site_seo_metni_tr = models.TextField(max_length=400,verbose_name="Seo Metni Türkçe")
    class Meta:
        verbose_name = "Şirket Seo Ayarı"
        verbose_name_plural = "Şirket Seo Ayarı"
class banner(models.Model):
    banner_basligi_tr =models.CharField(max_length=400,verbose_name="Banner Başliği Türkçe")
    banner_aciklama_tr = models.TextField(max_length=400,verbose_name="Banner Aciklama Türkçe")
    banner_sira = models.IntegerField(verbose_name="Banner Gösterme Sırası")
    banner_gosterme = models.BooleanField(verbose_name="Banner Gösterilsin mi ? ")
    banner_link = models.CharField(max_length=400,verbose_name="Bannera Link Brakmak İstiyorsanız link Ekleyin",null=True,blank=True)
    image  = models.ImageField(upload_to='banner/',blank = True,null = True,verbose_name="Sayfaya Banner Ekleyin")
    def save(self, *args, **kwargs):
        super(banner, self).save(*args, **kwargs)
        if self.image:
            with Image.open(self.image.path) as img:
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                width, height = img.size
                if width > 800:
                    new_width = 800
                    new_height = int((new_width / width) * height)
                    img = img.resize((new_width, new_height), Image.ANTIALIAS)
                    buffer = BytesIO()
                    img.save(buffer, format='JPEG', quality=60)
                    self.image.save(self.image.name, content=buffer, save=False)
                    super(banner, self).save(*args, **kwargs)
    class Meta:
        verbose_name = "Şirket Banner Ayarı"
        verbose_name_plural = "Şirket Banner Ayarı"

from ckeditor.fields import RichTextField
class hakkimizda(models.Model):
    hakkimizda_tr = RichTextField(verbose_name="Hakkımızda Yazısı Türkçe")
    class Meta:
        verbose_name = "Şirket Hakkımızda Yazısı"
        verbose_name_plural = "Şirket Hakkımızda Yazısı"
class anasayfa(models.Model):
    
    hakkimizda_tr = RichTextField(verbose_name="Anasayfa Yazısı Türkçe")
from django.utils.html import format_html
class site_renkleri(models.Model):
    renkbir = models.CharField(max_length=10,verbose_name="Renk Bir")
    renkiki = models.CharField(max_length=10,verbose_name="Renk İki")
    renkuc = models.CharField(max_length=10,verbose_name="Renk Üç")
    renkdort = models.CharField(max_length=10,verbose_name="Renk Dört") 
    class Meta:
        verbose_name = "Sayfa Renkleri"
        verbose_name_plural = "Sayfa Renkleri"
    def renkbir_goster(self):
        return format_html('<div style="width: 50px; height: 20px; background-color: {};"></div>', self.renkbir)
    renkbir_goster.short_description = 'Renk Bir'

    def renkiki_goster(self):
        return format_html('<div style="width: 50px; height: 20px; background-color: {};"></div>', self.renkiki)
    renkiki_goster.short_description = 'Renk İki'

    def renkuc_goster(self):
        return format_html('<div style="width: 50px; height: 20px; background-color: {};"></div>', self.renkuc)
    renkuc_goster.short_description = 'Renk Üç'

    def renkdort_goster(self):
        return format_html('<div style="width: 50px; height: 20px; background-color: {};"></div>', self.renkdort)
    renkdort_goster.short_description = 'Renk Dört'