from django.contrib import admin
from django.urls import path
from . import views

app_name = "admin_paneli"

urlpatterns = [
    path('girisyap/', views.admin_login),

]
