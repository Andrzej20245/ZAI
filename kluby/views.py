from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from kluby.models import Klub


def wszystkie(request):
    return HttpResponse(["<h1>", [[k.id, k.nazwa, k.liga] for k in Klub.objects.all()], "</h1>"])


def szczegoly(request, klub_id):
    k = Klub.objects.get(id=klub_id)
    return HttpResponse(
        "<h3> Nazwa klubu: {},</br> liga: {}, </br> miasto: {}, </br> rok powstania: {}, </br> wartość zespołu (w mln €): {}, </br> opis: {} </h3>"
        .format(k.nazwa, k.liga, k.miasto, k.rok_powstania, k.wartosc_zespolu, k.opis))



