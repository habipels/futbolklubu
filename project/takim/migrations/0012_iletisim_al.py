# Generated by Django 4.2.13 on 2024-07-05 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('takim', '0011_sponsorlar'),
    ]

    operations = [
        migrations.CreateModel(
            name='iletisim_al',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adi_soyadi', models.CharField(blank=True, max_length=200, null=True, verbose_name='Adı Soyadı')),
                ('numara', models.CharField(blank=True, max_length=200, null=True, verbose_name='Numarası')),
                ('konu', models.CharField(blank=True, max_length=200, null=True, verbose_name='konu')),
                ('mesaj', models.TextField(blank=True, verbose_name='Mesaj')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'İletişim',
                'verbose_name_plural': 'İletişim Kayıtları',
            },
        ),
    ]