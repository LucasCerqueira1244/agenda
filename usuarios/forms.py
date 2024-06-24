from django import forms
from .models import Reuniao

class ReuniaoForm(forms.ModelForm):
    class Meta:
        model = Reuniao
        fields = ['titulo', 'descricao', 'data', 'hora_inicio', 'hora_fim']
