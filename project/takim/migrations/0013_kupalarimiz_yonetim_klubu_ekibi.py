# Generated by Django 4.2.13 on 2024-07-28 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('takim', '0012_iletisim_al'),
    ]

    operations = [
        migrations.CreateModel(
            name='kupalarimiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adi_soyadi', models.CharField(blank=True, max_length=200, null=True, verbose_name=' Adı ')),
                ('dogum_tarihi', models.CharField(blank=True, max_length=200, null=True, verbose_name=' Tarihi')),
                ('aciklamasi', models.TextField(blank=True, verbose_name='Açıklaması')),
                ('fotografi', models.ImageField(upload_to='kupalarimiz/', verbose_name='Teknik Kadro')),
            ],
            options={
                'verbose_name': 'KUPALARIMIZ',
                'verbose_name_plural': 'KUPALARIMIZ',
            },
        ),
        migrations.CreateModel(
            name='yonetim_klubu_ekibi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adi_soyadi', models.CharField(blank=True, max_length=200, null=True, verbose_name=' Adı Soyadi')),
                ('dogum_tarihi', models.CharField(blank=True, max_length=200, null=True, verbose_name='Doğum Tarihi')),
                ('gorevi', models.CharField(blank=True, max_length=200, null=True, verbose_name='Görevi')),
                ('aciklamasi', models.TextField(blank=True, verbose_name='Açıklaması')),
                ('fotografi', models.ImageField(upload_to='yonetim/', verbose_name='Teknik Kadro')),
            ],
            options={
                'verbose_name': 'Yönetim KULÜBÜMÜZ',
                'verbose_name_plural': 'Yönetim KULÜBÜMÜZ',
            },
        ),
    ]