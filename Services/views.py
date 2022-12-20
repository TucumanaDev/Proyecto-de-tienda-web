from django.shortcuts import render
from .models import Services


def services(request):
    service = Services.objects.all()
    return render(request, "Services/services.html", {'services': service})


# Create your views here.
