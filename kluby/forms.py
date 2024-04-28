from django.forms import ModelForm, IntegerField, CharField
from .models import Klub, ExtraInfo, Sezon, Zawodnik
from django.core.validators import MinValueValidator

class KlubForm(ModelForm):
    rok_powstania = IntegerField(validators=[MinValueValidator(1850, message="Klub nie może być starszy niż z 1850 roku!!!!")])
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

class ExtraInfoFormWszystko(ModelForm):
    class Meta:
        model = ExtraInfo
        exclude = ['klub']


class SezonFormWszystko(ModelForm):
    class Meta:
        model = Sezon
        exclude = ['klub']

class ZawodnikFormWszystko(ModelForm):
    imie = CharField(label='Zawodnik: imię ')
    nazwisko = CharField(label='Zawodnik: nazwisko ')
    class Meta:
        model = Zawodnik
        fields = ['imie', 'nazwisko']

