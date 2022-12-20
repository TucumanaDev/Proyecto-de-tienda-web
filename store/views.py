from django.shortcuts import render
from django.shortcuts import render, redirect
from store.models import *

# Create your views here.

def store(request):
    products = Product.objects.all()
    categories = CategorieProd.objects.all()
    return render(request, "store/store.html", {"products": products, "categories": categories})

def categorie(request, categorie_id):
    categorie = CategorieProd.objects.get(id=categorie_id)
    categories = CategorieProd.objects.all()
    products = Product.objects.filter(categories = categorie)
    return render(request, "blog/categories.html", {"products" : products, "categories": categories,  "categorie": categorie})