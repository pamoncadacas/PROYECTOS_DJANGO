from django.contrib import admin
from .models import Cafeteria
# Register your models here.

class CafeteriaAdmin(admin.ModelAdmin):
    list_display = (
        "clasificacion",
        "producto",
        "calorias",
        "precio",
        "image",
    )
    
admin.site.register(Cafeteria, CafeteriaAdmin)
