# Generated by Django 4.1.2 on 2024-04-26 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('takim', '0003_u_11_skor_sayfasi_u_12_skor_sayfasi_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='teknik_kadro_ekibi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adi_soyadi', models.CharField(blank=True, max_length=200, null=True, verbose_name=' Adı Soyadi')),
                ('dogum_tarihi', models.CharField(blank=True, max_length=200, null=True, verbose_name='Doğum Tarihi')),
                ('aciklamasi', models.TextField(blank=True, verbose_name='Açıklaması')),
                ('fotografi', models.ImageField(upload_to='teknik_kadro/', verbose_name='Teknik Kadro')),
            ],
        ),
    ]