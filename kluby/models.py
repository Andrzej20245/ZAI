
from django.db import models


class Klub(models.Model):
    nazwa = models.CharField(max_length=64, blank=False, unique=True)
    liga = models.CharField(max_length=64, blank=False, unique=False)
    miasto = models.CharField(max_length=64, blank=True, unique=False)
    rok_powstania = models.PositiveSmallIntegerField(null=True, blank=True)
    wartosc_zespolu = models.DecimalField(max_digits=9, decimal_places=3, null=True, blank=True)
    opis = models.TextField(default="")


    def __str__(self):
        return "{} ({})".format(self.nazwa, self.liga)

class Zawodnik(models.Model):
    imie = models.CharField(max_length=64, blank=False, unique=False)
    nazwisko = models.CharField(max_length=64, blank=False, unique=False)
    klub = models.CharField(max_length=64, blank=True, unique=True)
    data_urodzenia = models.DateField(null=True, blank=True)
    wiek = models.PositiveSmallIntegerField(null=True, blank=True)
    opis = models.TextField(default="")

    def __str__(self):
        return "{} ({})".format(self.imie,self.nazwisko)
