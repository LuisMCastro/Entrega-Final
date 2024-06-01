from typing import Any

from django.db.models import Q
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from colaborador.forms import ColaboradorForm, ImagenForm
from colaborador.models import Colaborador, Imagen

####### COLABORADOR #######


class ColaboradorList(ListView):
    model = Colaborador
    template_name = "colaborador/colaborador_list.html"

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Colaborador.objects.filter(Q(nombre__icontains=busqueda))
        return queryset


class ColaboradorCreate(CreateView):
    model = Colaborador
    form_class = ColaboradorForm
    success_url = reverse_lazy("colaborador:colaborador_list")
    template_name = "colaborador/colaborador_form.html"


class ColaboradorDetail(DetailView):
    model = Colaborador
    template_name = "colaborador/colaborador_detail.html"


class ColaboradorUpdate(UpdateView):
    model = Colaborador
    form_class = ColaboradorForm
    success_url = reverse_lazy("colaborador:colaborador_list")
    template_name = "colaborador/colaborador_form.html"


class ColaboradorDelete(DeleteView):
    model = Colaborador
    success_url = reverse_lazy("colaborador:colaborador_list")
    template_name = "colaborador/colaborador_delete.html"


####### IMAGEN #######


class ImagenList(ListView):
    model = Imagen
    template_name = "imagen/imagen_list.html"

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Imagen.objects.filter(Q(nombre__icontains=busqueda))
        return queryset


class ImagenCreate(CreateView):
    model = Imagen
    form_class = ImagenForm
    success_url = reverse_lazy("imagen:imagen_list")
    template_name = "imagen/imagen_form.html"


class ImagenDetail(DetailView):
    model = Imagen
    template_name = "imagen/imagen_detail.html"


class ImagenUpdate(UpdateView):
    model = Imagen
    form_class = ImagenForm
    success_url = reverse_lazy("imagen:imagen_list")
    template_name = "imagen/imagen_form.html"


class ImagenDelete(DeleteView):
    model = Imagen
    success_url = reverse_lazy("imagen:imagen_list")
    template_name = "imagen/imagen_delete.html"
