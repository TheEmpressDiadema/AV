from django.urls import path
from . import views
'''
TODO:
Сформировать маршрутизацию для ListView классов:
CarList,
BrandList,
ModelList,
GenerationList
'''
urlpatterns = [
    path('', views.BrandList.as_view(), name='home'),
    path('add-brand/', views.AddBrand.as_view(), name='add_brand')
]