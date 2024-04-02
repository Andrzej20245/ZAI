from django.forms import ModelForm
from .models import Klub


class KlubForm(ModelForm):
    class Meta:
        model = Klub
        fields = ['nazwa', 'miasto', 'rok_powstania', 'opis']