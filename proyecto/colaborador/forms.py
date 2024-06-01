from django import forms

from . import models


class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = models.Colaborador
        fields = "__all__"
        localized_fields = ("foto_perfil",)


class ImagenForm(forms.ModelForm):
    class Meta:
        model = models.Imagen
        fields = "__all__"
