from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Services import views

urlpatterns = [
    path('', views.services, name="services")
]

