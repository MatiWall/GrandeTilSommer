from django.forms import ModelForm

from .models import MacroCycle

class MacroForm(ModelForm):

    class Meta:
        model = MacroCycle
        fields = ('name', 'description', 'duration')

