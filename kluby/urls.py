"""
URL configuration for footballweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from kluby.views import portal, wszystkie, szczegoly, nowy, edytuj, usun,nowy_wszystko,\
    extra_wszystkie, extra_szczegoly, extra_nowy, extra_edytuj,extra_usun, \
    sezon_wszystkie, sezon_szczegoly, sezon_nowy,sezon_edytuj,sezon_usun, \
    zawodnik_wszystkie, zawodnik_szczegoly, zawodnik_nowy, zawodnik_edytuj, zawodnik_usun



urlpatterns = [
    path('portal/',portal, name='portal'),
    path('portal/klub_wszystkie/',wszystkie, name='wszystkie'),
    path('portal/klub_szczegoly/<int:klub_id>/',szczegoly, name='szczegoly'),
    path('portal/klub_nowy/', nowy, name='nowy'),
    path('portal/klub_edytuj/<int:klub_id>/', edytuj, name='edytuj'),
    path('portal/klub_usun/<int:klub_id>/', usun, name='usun'),
    path('portal/klub_nowy_wszystko/', nowy_wszystko, name='nowy_wszystko'),
    path('portal/extra_wszystkie/',extra_wszystkie, name='extra_wszystkie'),
    path('portal/extra_szczegoly/<int:extra_id>/',extra_szczegoly, name='extra_szczegoly'),
    path('portal/extra_nowy/', extra_nowy, name='extra_nowy'),
    path('portal/extra_edytuj/<int:extra_id>/', extra_edytuj, name='extra_edytuj'),
    path('portal/extra_usun/<int:extra_id>/', extra_usun, name='extra_usun'),
    path('portal/sezon_wszystkie/', sezon_wszystkie, name='sezon_wszystkie'),
    path('portal/sezon_szczegoly/<int:sezon_id>/', sezon_szczegoly, name='sezon_szczegoly'),
    path('portal/sezon_nowy/', sezon_nowy, name='sezon_nowy'),
    path('portal/sezon_edytuj/<int:sezon_id>/', sezon_edytuj, name='sezon_edytuj'),
    path('portal/sezon_usun/<int:sezon_id>/', sezon_usun, name='sezon_usun'),
    path('portal/zawodnik_wszystkie/', zawodnik_wszystkie, name='zawodnik_wszystkie'),
    path('portal/zawodnik_szczegoly/<int:zawodnik_id>/', zawodnik_szczegoly, name='zawodnik_szczegoly'),
    path('portal/zawodnik_nowy/', zawodnik_nowy, name='zawodnik_nowy'),
    path('portal/zawodnik_edytuj/<int:zawodnik_id>/', zawodnik_edytuj, name='zawodnik_edytuj'),
    path('portal/zawodnik_usun/<int:zawodnik_id>/', zawodnik_usun, name='zawodnik_usun'),
]
