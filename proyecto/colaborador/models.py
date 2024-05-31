from django.contrib.auth.models import User
from django.db import models
from django.forms import ValidationError
from django.utils import timezone


class Colaborador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Colaborador", unique=True)
    edad = models.PositiveIntegerField()
    GENEROS = [("M", "Mujer"), ("H", "Hombre"), ("NB", "No Binario")]
    genero = models.CharField(max_length=100, choices=GENEROS, default="Hombre")
    foto_perfil = models.ImageField(upload_to="fotos_perfil", null=True, blank=True)
    biografia = models.TextField(blank=False, null=False)
    fecha_registro = models.DateTimeField(editable=False, default=timezone.now)

    class Meta:
        verbose_name = "Colaborador"
        verbose_name_plural = "Colaboradores"

    def __str__(self):
        return f"{self.usuario.username}."

    def clean(self):
        if self.edad < 18:
            raise ValidationError("Usted no puede ser menor de 18 años")


class Imagen(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.SET_NULL, null=True, blank=True)
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True)
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(blank=False, null=False)
    fecha_subida = models.DateTimeField(editable=False, default=timezone.now)

    class Meta:
        ordering = ("fecha_subida",)
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"

    def __str__(self):
        return f"{self.titulo}, by {self.colaborador}"
