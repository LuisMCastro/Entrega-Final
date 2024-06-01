from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import CustomAuthentificationForm, CustomUserCreationForm


def home_index(request):
    return render(request, "home/index.html")
    # return reverse_lazy("home:index")


def about(request):
    return render(request, "home/about.html")
    # return reverse_lazy("home:index")


class CustomLoginView(LoginView):
    authentication_form = CustomAuthentificationForm
    template_name = "home/login.html"


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "home/index.html", {"mensaje": f"Usuario '{username}' creado"})
        ...
    else:
        form = CustomUserCreationForm()
    return render(request, "home/register.html", {"form": form})
