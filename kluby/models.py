
from django.db import models


class Klub(models.Model):
    nazwa = models.CharField(max_length=64, blank=False, unique=True)
    miasto = models.CharField(max_length=64, blank=True, unique=False)
    rok_powstania = models.PositiveSmallIntegerField(null=True, blank=True)
    opis = models.TextField(default="")


    def __str__(self):
        return "{} ({})".format(self.nazwa, self.miasto)


class ExtraInfo(models.Model):
    LIGA = {
        (0, 'Bundesliga'),
        (1, 'Premier League'),
        (2, 'Serie A'),
        (3, 'La Liga'),
        (4, 'Ekstraklasa')
    }

    liga = models.PositiveSmallIntegerField(choices=LIGA, null=True, blank=True)
    wartosc_zespolu = models.DecimalField(max_digits=9, decimal_places=3, null=True, blank=True)
    trener = models.CharField(max_length=50, blank=True, null=True)
    klub = models.OneToOneField(Klub, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        for l in list(self.LIGA):
            if l[0] == self.liga:
                lok = l[1]
        return "Klub: {}, liga: {}, wartość zespołu: {} mln €, trener: {}".format(self.klub.nazwa,lok, self.wartosc_zespolu, self.trener)

class Sezon(models.Model):
    opinia = models.TextField(default="", blank=True)
    start = models.DateField(null=True, blank=True)
    koniec = models.DateField(null=True, blank=True)
    klub = models.ForeignKey(Klub, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        op = self.opinia[:20] + ' ...'
        return "Klub: {}, okres od: {}, okres do : {}, opinia: {}".format(self.klub.nazwa, str(self.start),str(self.koniec), op)

class Zawodnik(models.Model):
    imie = models.CharField(max_length=64, blank=False, unique=False)
    nazwisko = models.CharField(max_length=64, blank=False, unique=False)
    wiek = models.PositiveSmallIntegerField(null=True, blank=True)
    kluby = models.ManyToManyField(Klub)

    def __str__(self):
        return "{} {}, gra w {} klubach z bazy danych".format(self.imie, self.nazwisko, str(self.kluby.count()))
