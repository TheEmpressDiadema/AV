from rest_framework import generics

from .serializers import (
    EngineSerializer, 
    CarSerializer, 
    GenSerializer, 
    CarModelSerializer, 
    BrandSerializer,
    CarImageSerializer)

from .models import (
    Brand, CarModel, 
    Gen, Engine, 
    Car, CarImage
)

class BrandAPIView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class ModelAPIView(generics.ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

class GenAPIView(generics.ListAPIView):
    queryset = Gen.objects.all()
    serializer_class = GenSerializer

class EngineAPIView(generics.ListAPIView):
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer

class CarAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarImageAPIView(generics.ListAPIView):
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer