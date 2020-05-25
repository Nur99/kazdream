from django.contrib import admin
from .models import Car, Color, Manufacturer


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'color', 'manufacturer', )
    list_filter = ('color__name', 'manufacturer__name')


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
