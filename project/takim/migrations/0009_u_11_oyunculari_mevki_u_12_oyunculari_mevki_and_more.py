# Generated by Django 4.1.2 on 2024-04-27 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('takim', '0008_u_11_oyunculari_u_12_oyunculari_u_13_oyunculari'),
    ]

    operations = [
        migrations.AddField(
            model_name='u_11_oyunculari',
            name='mevki',
            field=models.CharField(blank=True, max_length=200, verbose_name='mevki'),
        ),
        migrations.AddField(
            model_name='u_12_oyunculari',
            name='mevki',
            field=models.CharField(blank=True, max_length=200, verbose_name='mevki'),
        ),
        migrations.AddField(
            model_name='u_13_oyunculari',
            name='mevki',
            field=models.CharField(blank=True, max_length=200, verbose_name='mevki'),
        ),
    ]