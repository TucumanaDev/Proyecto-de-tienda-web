from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('categories/<int:categorie_id>/', views.categorie, name="categorie")
]
