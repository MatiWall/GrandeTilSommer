from django.forms import ModelForm, formset_factory, inlineformset_factory

from .models import MacroCycle, MesoCycle

class MacroForm(ModelForm):
    class Meta:
        model = MacroCycle
        fields = ('name', 'description', 'duration')

class MesoForm(ModelForm):
    class Meta:
        model = MesoCycle
        fields = ('name', 'description', 'duration')


