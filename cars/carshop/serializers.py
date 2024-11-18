from rest_framework import serializers
from .models import Car, Gen, CarModel, Brand, Engine, CarImage

class EngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = ['name', 'fuel_type', 'volume', 'power', 'milage', 'created', 'updated']

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['name', 'gen', 'engine', 'vin', 'price', 'color', 'description', 'images', 'slug','created', 'updated']

class GenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gen
        fields = ['name', 'model', 'slug', 'image', 'release_start', 'release_end','created', 'updated']

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['name', 'brand', 'slug', 'created', 'updated']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'slug', 'created', 'updated']

class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ['car', 'image', 'created']