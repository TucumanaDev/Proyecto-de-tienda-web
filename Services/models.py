from django.db import models

# Create your models here.


class Services(models.Model):
    title = models.CharField(max_length=35)
    content = models.CharField(max_length=35)
    image = models.ImageField(upload_to='Services')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.title
