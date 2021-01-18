from django.contrib import admin

# Register your models here.
from .models import Manufacturer, CPU, Motherboard

admin.site.register(Motherboard)
admin.site.register(CPU)
admin.site.register(Manufacturer)




