from django.urls import path

from home.views import home_index

app_name = "home"

urlpatterns = [
    path("", home_index, name="index"),
]
