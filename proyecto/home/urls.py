from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path

from home.views import CustomLoginView, about, home_index, register

app_name = "home"

urlpatterns = [
    path("", home_index, name="index"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="home/logout.html"), name="logout"),
    path("register/", register, name="register"),
    path("about/", about, name="about"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
