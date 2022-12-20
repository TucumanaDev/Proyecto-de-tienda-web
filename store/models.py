from django.db import models

# Create your models here.

class CategorieProd(models.Model):
    name = models.CharField(max_length = 50)
    created = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name = "CategorieProd"
        verbose_name_plural = "CategoriesProd"
        
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length = 50)
    categories = models.ForeignKey(CategorieProd, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "store", null = True, blank = True)
    price = models.FloatField()
    availability = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now_add = True)
    
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"