from django.shortcuts import render
from django.urls import reverse_lazy


def home_index(request):
    return render(request, "home/index.html")
    # return reverse_lazy("home:index")
