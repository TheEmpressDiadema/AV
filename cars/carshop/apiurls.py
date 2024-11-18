from django.urls import path
from . import apiviews

urlpatterns = [
    path('brands/', apiviews.BrandAPIView.as_view(), name="api_brands"),
    path('car-models/', apiviews.ModelAPIView.as_view(), name="api_models"),
    path('gens/', apiviews.GenAPIView.as_view(), name='api_gens'),
    path('cars/', apiviews.CarAPIView.as_view(), name='api_cars'),
    path('engines/', apiviews.EngineAPIView.as_view(), name='api_engines'),
    path('car-images/', apiviews.CarImageAPIView.as_view(), name="api_car_images")
]