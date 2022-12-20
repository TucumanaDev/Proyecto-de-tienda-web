from django.shortcuts import render, HttpResponse
from Services.models import Services


# Create your views here.
def home(request):
    return render(request, "WebProjectApp/home.html")


def store(request):
    return render(request, "WebProjectApp/store.html")
