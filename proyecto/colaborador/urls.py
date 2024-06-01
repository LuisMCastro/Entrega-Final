from django.urls import path

from colaborador.views import (
    ColaboradorCreate,
    ColaboradorDelete,
    ColaboradorDetail,
    ColaboradorList,
    ColaboradorUpdate,
    ImagenCreate,
    ImagenDelete,
    ImagenDetail,
    ImagenList,
    ImagenUpdate,
)

app_name = "colaborador"

urlpatterns = [
    path("colaborador/list", ColaboradorList.as_view(), name="colaborador_list"),
    path("colaborador/create", ColaboradorCreate.as_view(), name="colaborador_create"),
    path("colaborador/detail/<int:pk>", ColaboradorDetail.as_view(), name="colaborador_detail"),
    path("colaborador/update/<int:pk>", ColaboradorUpdate.as_view(), name="colaborador_update"),
    path("colaborador/delete/<int:pk>", ColaboradorDelete.as_view(), name="colaborador_delete"),
]

urlpatterns += [
    path("imagen/list", ImagenList.as_view(), name="imagen_list"),
    path("imagen/create", ImagenCreate.as_view(), name="imagen_create"),
    path("imagen/detail/<int:pk>", ImagenDetail.as_view(), name="imagen_detail"),
    path("imagen/update/<int:pk>", ImagenUpdate.as_view(), name="imagen_update"),
    path("imagen/delete/<int:pk>", ImagenDelete.as_view(), name="imagen_delete"),
]
