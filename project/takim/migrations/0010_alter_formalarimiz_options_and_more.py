# Generated by Django 4.1.2 on 2024-06-01 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('takim', '0009_u_11_oyunculari_mevki_u_12_oyunculari_mevki_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formalarimiz',
            options={'verbose_name': 'Formalarımız', 'verbose_name_plural': 'Formalarımız'},
        ),
        migrations.AlterModelOptions(
            name='teknik_kadro_ekibi',
            options={'verbose_name': 'Teknik Kadro Ekibi', 'verbose_name_plural': 'Teknik Kadro Ekibi'},
        ),
        migrations.AlterModelOptions(
            name='u_11_fotograflari',
            options={'verbose_name': 'U-11 Fotoğraflarımız', 'verbose_name_plural': 'U-11 Fotoğraflarımız'},
        ),
        migrations.AlterModelOptions(
            name='u_11_oyunculari',
            options={'verbose_name': 'U-11 Oyuncularımız', 'verbose_name_plural': 'U-11 Oyuncularımız'},
        ),
        migrations.AlterModelOptions(
            name='u_11_skor_sayfasi',
            options={'verbose_name': 'U-11 TFF Bilgi Sayfası', 'verbose_name_plural': 'U-11 TFF Bilgi Sayfası'},
        ),
        migrations.AlterModelOptions(
            name='u_11_takimi_son_karsilasma',
            options={'verbose_name': 'U-11 Takım Son Karşılaşması', 'verbose_name_plural': 'U-11 Takım Son Karşılaşması'},
        ),
        migrations.AlterModelOptions(
            name='u_12_fotograflari',
            options={'verbose_name': 'U-12 Fotoğraflarımız', 'verbose_name_plural': 'U-12 Fotoğraflarımız'},
        ),
        migrations.AlterModelOptions(
            name='u_12_oyunculari',
            options={'verbose_name': 'U-12 Oyuncularımız', 'verbose_name_plural': 'U-12 Oyuncularımız'},
        ),
        migrations.AlterModelOptions(
            name='u_12_skor_sayfasi',
            options={'verbose_name': 'U-12 TFF Bilgi Sayfası', 'verbose_name_plural': 'U-12 TFF Bilgi Sayfası'},
        ),
        migrations.AlterModelOptions(
            name='u_12_takimi_son_karsilasma',
            options={'verbose_name': 'U-12 Takım Son Karşılaşması', 'verbose_name_plural': 'U-12 Takım Son Karşılaşması'},
        ),
        migrations.AlterModelOptions(
            name='u_13_fotograflari',
            options={'verbose_name': 'U-13 Fotoğraflarımız', 'verbose_name_plural': 'U-13 Fotoğraflarımız'},
        ),
        migrations.AlterModelOptions(
            name='u_13_oyunculari',
            options={'verbose_name': 'U-13 Oyuncularımız', 'verbose_name_plural': 'U-13 Oyuncularımız'},
        ),
        migrations.AlterModelOptions(
            name='u_13_skor_sayfasi',
            options={'verbose_name': 'U-13 TFF Bilgi Sayfası', 'verbose_name_plural': 'U-13 TFF Bilgi Sayfası'},
        ),
        migrations.AlterModelOptions(
            name='u_13_takimi_son_karsilasma',
            options={'verbose_name': 'U-13 Takım Son Karşılaşması', 'verbose_name_plural': 'U-13 Takım Son Karşılaşması'},
        ),
        migrations.AlterField(
            model_name='formalarimiz',
            name='aciklamasi',
            field=models.TextField(blank=True, verbose_name='Açıklama'),
        ),
        migrations.AlterField(
            model_name='u_11_fotograflari',
            name='aciklamasi',
            field=models.TextField(blank=True, verbose_name='Açıklama'),
        ),
        migrations.AlterField(
            model_name='u_12_fotograflari',
            name='aciklamasi',
            field=models.TextField(blank=True, verbose_name='Açıklama'),
        ),
        migrations.AlterField(
            model_name='u_13_fotograflari',
            name='aciklamasi',
            field=models.TextField(blank=True, verbose_name='Açıklma'),
        ),
    ]
