from django.db import models

# Create your models here.
class u_11_takimi_son_karsilasma(models.Model):
    maglub_galibiyet = (("",""),("MAĞLUP","MAĞLUP"),
                        ("KAZANAN","KAZANAN"))
    ev_sahibi_takim_adi = models.CharField(max_length = 200,verbose_name = "Ev SAhibi Takım",blank = True,null = True)
    ev_sahibi_takim_logusu = models.CharField(max_length = 1000,verbose_name = "Ev SAhibi Takım Logusu Link",blank = True,null = True) 
    ev_sahibi_kazanma_kaybetme = models.CharField(max_length=200,blank = True,null = True, choices=maglub_galibiyet, default='')
    ev_sahibi_skoru = models.CharField(max_length = 200,verbose_name = "Ev SAhibi Skoru",blank = True,null = True)
    ev_sahibi_gol_atanlar = models.TextField(verbose_name = "Ev Sahibi Gol Atanlar",blank = True,null = True)
    karsilasma_tarihi = models.TextField(verbose_name = "Karşılaşma Tarihi",blank = True,null = True)
    karsilasma_yeri = models.TextField(verbose_name = "Karşılaşma yeri",blank = True,null = True)
    deplasman_takim_adi = models.CharField(max_length = 200,verbose_name = "Deplasman Takım",blank = True,null = True)
    deplasman_takim_logusu = models.CharField(max_length = 1000,verbose_name = "Deplasman Takım Logusu Link",blank = True,null = True) 
    deplasman_kazanma_kaybetme = models.CharField(max_length=200,blank = True,null = True, choices=maglub_galibiyet, default='')
    deplasman_skoru = models.CharField(max_length = 200,verbose_name = "Deplasman Skoru",blank = True,null = True)
    deplasman_gol_atanlar = models.TextField(verbose_name = "Deplasman Gol Atanlar",blank = True,null = True)    

class u_12_takimi_son_karsilasma(models.Model):
    maglub_galibiyet = (("",""),("MAĞLUP","MAĞLUP"),
                        ("KAZANAN","KAZANAN"))
    ev_sahibi_takim_adi = models.CharField(max_length = 200,verbose_name = "Ev SAhibi Takım",blank = True,null = True)
    ev_sahibi_takim_logusu = models.CharField(max_length = 1000,verbose_name = "Ev SAhibi Takım Logusu Link",blank = True,null = True) 
    ev_sahibi_kazanma_kaybetme = models.CharField(max_length=200,blank = True,null = True, choices=maglub_galibiyet, default='')
    ev_sahibi_skoru = models.CharField(max_length = 200,verbose_name = "Ev SAhibi Skoru",blank = True,null = True)
    ev_sahibi_gol_atanlar = models.TextField(verbose_name = "Ev Sahibi Gol Atanlar",blank = True,null = True)
    karsilasma_tarihi = models.TextField(verbose_name = "Karşılaşma Tarihi",blank = True,null = True)
    karsilasma_yeri = models.TextField(verbose_name = "Karşılaşma yeri",blank = True,null = True)
    deplasman_takim_adi = models.CharField(max_length = 200,verbose_name = "Deplasman Takım",blank = True,null = True)
    deplasman_takim_logusu = models.CharField(max_length = 1000,verbose_name = "Deplasman Takım Logusu Link",blank = True,null = True) 
    deplasman_kazanma_kaybetme = models.CharField(max_length=200,blank = True,null = True, choices=maglub_galibiyet, default='')
    deplasman_skoru = models.CharField(max_length = 200,verbose_name = "Deplasman Skoru",blank = True,null = True)
    deplasman_gol_atanlar = models.TextField(verbose_name = "Deplasman Gol Atanlar",blank = True,null = True)    
class u_13_takimi_son_karsilasma(models.Model):
    maglub_galibiyet = (("",""),("MAĞLUP","MAĞLUP"),
                        ("KAZANAN","KAZANAN"))
    ev_sahibi_takim_adi = models.CharField(max_length = 200,verbose_name = "Ev SAhibi Takım",blank = True,null = True)
    ev_sahibi_takim_logusu = models.CharField(max_length = 1000,verbose_name = "Ev SAhibi Takım Logusu Link",blank = True,null = True) 
    ev_sahibi_kazanma_kaybetme = models.CharField(max_length=200,blank = True,null = True, choices=maglub_galibiyet, default='')
    ev_sahibi_skoru = models.CharField(max_length = 200,verbose_name = "Ev SAhibi Skoru",blank = True,null = True)
    ev_sahibi_gol_atanlar = models.TextField(verbose_name = "Ev Sahibi Gol Atanlar",blank = True,null = True)
    karsilasma_tarihi = models.TextField(verbose_name = "Karşılaşma Tarihi",blank = True,null = True)
    karsilasma_yeri = models.TextField(verbose_name = "Karşılaşma yeri",blank = True,null = True)
    deplasman_takim_adi = models.CharField(max_length = 200,verbose_name = "Deplasman Takım",blank = True,null = True)
    deplasman_takim_logusu = models.CharField(max_length = 1000,verbose_name = "Deplasman Takım Logusu Link",blank = True,null = True) 
    deplasman_kazanma_kaybetme = models.CharField(max_length=200,blank = True,null = True, choices=maglub_galibiyet, default='')
    deplasman_skoru = models.CharField(max_length = 200,verbose_name = "Deplasman Skoru",blank = True,null = True)
    deplasman_gol_atanlar = models.TextField(verbose_name = "Deplasman Gol Atanlar",blank = True,null = True)    

class u_11_skor_sayfasi(models.Model):
    url_bilgisi = models.CharField(max_length = 400,verbose_name = "u - 11 tff sayfa linki")


class u_12_skor_sayfasi(models.Model):
    url_bilgisi = models.CharField(max_length = 400,verbose_name = "u - 12 tff sayfa linki")


class u_13_skor_sayfasi(models.Model):
    url_bilgisi = models.CharField(max_length = 400,verbose_name = "u - 13 tff sayfa linki")