from django.forms import ModelForm

from .models import MacroCycle, MesoCycle

class MacroForm(ModelForm):
    class Meta:
        model = MacroCycle
        fields = ('name', 'description', 'duration')

class MesoForm(ModelForm):
    class Meta:
        model = MesoCycle
        fields = ('name', 'description', 'duration')
