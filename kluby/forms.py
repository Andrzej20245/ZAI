from django.forms import ModelForm, IntegerField, CharField
from .models import Klub, ExtraInfo, Sezon, Zawodnik
from django.core.validators import MinValueValidator

class KlubForm(ModelForm):
    class Meta:
        model = Klub
        fields = ['nazwa', 'miasto', 'rok_powstania', 'opis']


class KlubFormNowy(ModelForm):
    rok_powstania = IntegerField(validators=[MinValueValidator(2010, message="Założenie klubu nie moze być starsze niz  2010 rok! ")])
    class Meta:
        model = Klub
        fields = ['nazwa', 'miasto', 'rok_powstania', 'opis']


class ExtraInfoForm(ModelForm):
    class Meta:
        model = ExtraInfo
        fields = '__all__'
class SezonForm(ModelForm):
    class Meta:
        model = Sezon
        fields = '__all__'

class ZawodnikForm(ModelForm):
    class Meta:
        model = Zawodnik
        fields = '__all__'

class ExtraInfoForm2(ModelForm):
    class Meta:
        model = ExtraInfo
        exclude = ['klub']


class SezonForm2(ModelForm):
    class Meta:
        model = Sezon
        exclude = ['klub']

class ZawodnikForm2(ModelForm):
    imie = CharField(label='Zawodnik: imię ')
    nazwisko = CharField(label='Zawodnik: nazwisko ')
    class Meta:
        model = Zawodnik
        fields = ['imie', 'nazwisko']

