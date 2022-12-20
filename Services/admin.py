from django.contrib import admin
from .models import Services

# Register your models here.


class datetimeAdmin(admin.ModelAdmin):
    readonly_fields = ('update', 'created')


admin.site.register(Services, datetimeAdmin)