from django import forms

from . import models


class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = models.Colaborador
        fields = "__all__"
