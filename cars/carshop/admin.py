from .models import Brand, CarModel, Gen, Engine, Car, CarImage

from django.contrib import admin

# Register your models here.
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created', 'updated')
    list_display_links = ('name', 'slug')
    ordering = ['-created']

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'slug', 'created', 'updated')
    list_display_links = ('name', 'slug')
    ordering = ['-created']

@admin.register(Gen)
class GenAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model', 'image', 'release_start', 'release_end', 'slug', 'created', 'updated')
    list_display_links = ('name', 'slug')
    ordering = ['-created']

@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = ('name', 'fuel_type', 'volume', 'power', 'created', 'updated')
    list_display_links = ('name',)
    ordering = ['-created']

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'gen', 'engine', 'milage', 'vin', 'price', 'color', 'description', 'slug', 'created', 'updated')
    list_display_links = ('name', 'slug')
    ordering = ['-created']

@admin.register(CarImage)
class CarImage(admin.ModelAdmin):
    list_display = ('car', 'image', 'created')
    list_display_links = ('image',)
    ordering = ['created']