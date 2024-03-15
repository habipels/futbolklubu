from django import template 
from django.utils.safestring import mark_safe
from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from site_settings.models import *
from takim.models import *
register = template.Library()
import requests
from bs4 import BeautifulSoup

#@register.filter
@register.simple_tag
def u_12():
    content=[]
    url = u_12_skor_sayfasi.objects.last().url_bilgisi
    # URL'den HTML içeriğini çek
    response = requests.get(url)
    html_content = response.text
    # BeautifulSoup ile HTML'i analiz et
    soup = BeautifulSoup(html_content, 'html.parser')

    # Örneğin tüm <p> etiketlerini alalım
    paragraflar = soup.find_all('li',class_ = "widget-results__item")
    # Her bir paragrafı yazdıralım
    """"""
    tarihler = []
    for index, paragraf in enumerate(paragraflar):
        if (paragraf.find("div", class_="widget-results__title")):
            tarihler.append(paragraf.find("div", class_="widget-results__title").text)
    for index, paragraf in enumerate(paragraflar):
        c = 0
        sozluk = {}  # Her paragraf için yeni bir sözlük oluştur
        liste  = []
        for i in paragraf.find_all("h5", class_="widget-results__team-name"):
            liste.append(i.text)
        for i in paragraf.find_all("div", class_="widget-results__stadiumname"):
            sozluk[f"mac_yeri"] = i.text
        
        resim_list = []
        for i in paragraf.find_all("figure",class_ = "widget-results__team-logo"):
            a = i.find("img")
            if a:
                x = "https://tffistanbul.org"+a["src"]
                resim_list.append(x)   
        if  liste: 
            sozluk[f"takim"] = liste
        if resim_list:
            sozluk["logo"] = resim_list
        for j in range(len(tarihler)):
            if c == j:
                sozluk[f"tarih"] = tarihler[j]
        if  liste: 
            content.append(sozluk)  # content sözlüğüne her bir sözlük ekleniyor
            c = c+1
        
    return content


@register.simple_tag
def u_11():
    content={}
    url = u_11_skor_sayfasi.objects.last().url_bilgisi
    # URL'den HTML içeriğini çek
    response = requests.get(url)
    html_content = response.text
    # BeautifulSoup ile HTML'i analiz et
    soup = BeautifulSoup(html_content, 'html.parser')

    # Örneğin tüm <p> etiketlerini alalım
    paragraflar = soup.find_all('li',class_ = "widget-results__item")
    # Her bir paragrafı yazdıralım
    """"""
    tarihler = []
    for index, paragraf in enumerate(paragraflar):
        if (paragraf.find("div", class_="widget-results__title")):
            tarihler.append(paragraf.find("div", class_="widget-results__title").text)
    for index, paragraf in enumerate(paragraflar):
        c = 0
        sozluk = {}  # Her paragraf için yeni bir sözlük oluştur
        liste  = []
        for i in paragraf.find_all("h5", class_="widget-results__team-name"):
            liste.append(i.text)
        for i in paragraf.find_all("div", class_="widget-results__stadiumname"):
            sozluk[f"mac_yeri"] = i.text
        
        resim_list = []
        for i in paragraf.find_all("figure",class_ = "widget-results__team-logo"):
            a = i.find("img")
            if a:
                x = "https://tffistanbul.org"+a["src"]
                resim_list.append(x)   
        if  liste: 
            sozluk[f"takim"] = liste
        if resim_list:
            sozluk["logo"] = resim_list
        for j in range(len(tarihler)):
            if c == j:
                sozluk[f"tarih"] = tarihler[j]
        if  liste: 
            content[index] = sozluk  # content sözlüğüne her bir sözlük ekleniyor
            c = c+1

    return content
@register.simple_tag
def u_13():
    content={}
    url = u_13_skor_sayfasi.objects.last().url_bilgisi
    # URL'den HTML içeriğini çek
    response = requests.get(url)
    html_content = response.text
    # BeautifulSoup ile HTML'i analiz et
    soup = BeautifulSoup(html_content, 'html.parser')

    # Örneğin tüm <p> etiketlerini alalım
    paragraflar = soup.find_all('li',class_ = "widget-results__item")
    # Her bir paragrafı yazdıralım
    """"""
    tarihler = []
    for index, paragraf in enumerate(paragraflar):
        if (paragraf.find("div", class_="widget-results__title")):
            tarihler.append(paragraf.find("div", class_="widget-results__title").text)
    for index, paragraf in enumerate(paragraflar):
        c = 0
        sozluk = {}  # Her paragraf için yeni bir sözlük oluştur
        liste  = []
        for i in paragraf.find_all("h5", class_="widget-results__team-name"):
            liste.append(i.text)
        for i in paragraf.find_all("div", class_="widget-results__stadiumname"):
            sozluk[f"mac_yeri"] = i.text
        
        resim_list = []
        for i in paragraf.find_all("figure",class_ = "widget-results__team-logo"):
            a = i.find("img")
            if a:
                x = "https://tffistanbul.org"+a["src"]
                resim_list.append(x)   
        if  liste: 
            sozluk[f"takim"] = liste
        if resim_list:
            sozluk["logo"] = resim_list
        for j in range(len(tarihler)):
            if c == j:
                sozluk[f"tarih"] = tarihler[j]
        if  liste: 
            content[index] = sozluk  # content sözlüğüne her bir sözlük ekleniyor
            c = c+1

    return content