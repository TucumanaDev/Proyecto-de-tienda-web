from django.contrib import admin
from .models import Category, Post

# Register your models here.


class CategorieAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')


admin.site.register(Category, CategorieAdmin)
admin.site.register(Post, PostAdmin)