from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("about", views.about, name="about"),
    path("galery", views.fotograflar, name="fotograflar"),
    path("u11galery", views.u_11, name="u_11"),
    path("u12galery", views.u_12, name="u_12"),
    path("u13galery", views.u_13, name="u_13"),
    path("ourtechnicalstaff", views.teknik_kadromuz, name="teknik_kadromuz"),
]