from django.contrib.auth.models import User
from django.db import models
from django.forms import ValidationError
from django.utils import timezone


class Colaborador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Colaborador")
    edad = models.PositiveIntegerField(max_length=2)
    GENEROS = [("M", "Mujer"), ("H", "Hombre"), ("NB", "No Binario")]
    genero = models.CharField(max_length=1, choices=GENEROS, default="Hombre")
    foto_perfil = models.ImageField(upload_to="fotos_perfil", null=True, blank=True)
    descripcion = models.TextField(blank=False, null=False)
    fecha_registro = models.DateTimeField(editable=False, default=timezone.now)


def __str__(self):
    return f"{self.usuario.username}, {self.edad} años, {self.genero}."


def clean(self):
    if self.edad < 18:
        raise ValidationError("Usted no puede ser menor de 18 años")
