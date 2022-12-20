from django.shortcuts import render
from blog.models import *

# Create your views here.


def blog(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, "blog/blog.html", {"posts" : posts, "categories": categories})


def categorie(request, categorie_id):
    categorie = Category.objects.get(id=categorie_id)
    categories = Category.objects.all()
    posts = Post.objects.filter(categories = categorie)
    return render(request, "blog/categories.html", {"posts" : posts, "categories": categories,  "categorie": categorie})