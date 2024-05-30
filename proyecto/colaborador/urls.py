from django.urls import path

from colaborador.views import (
    ColaboradorCreate,
    ColaboradorDelete,
    ColaboradorDetail,
    ColaboradorList,
    ColaboradorUpdate,
)

app_name = "colaborador"

urlpatterns = [
    path("colaborador/list", ColaboradorList.as_view(), name="colaborador_list"),
    path("colaborador/create", ColaboradorCreate.as_view(), name="colaborador_create"),
    path("colaborador/detail/<int:pk>", ColaboradorDetail.as_view(), name="colaborador_detail"),
    path("colaborador/update/<int:pk>", ColaboradorUpdate.as_view(), name="colaborador_update"),
    path("colaborador/delete/<int:pk>", ColaboradorDelete.as_view(), name="colaborador_delete"),
]
