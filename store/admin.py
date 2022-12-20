from django.contrib import admin
from .models import CategorieProd, Product
# Register your models here.

class CategorieProdAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "update")
    
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "update")
    
admin.site.register(CategorieProd, CategorieProdAdmin)
admin.site.register(Product, ProductAdmin)

