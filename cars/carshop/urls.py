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
    path('', views.IndexView.as_view(), name='home'),
    path('brand-list/', views.BrandList.as_view(), name='brand_list'),
    path('add-brand/', views.AddBrand.as_view(), name='add_brand'),
    path('edit/<slug:brand_slug>', views.UpdateBrand.as_view(), name='edit_brand'),
    path('brand/<slug:brand_slug>/model-list/', views.ModelList.as_view(), name='model_list'),
    path('brand/<slug:brand_slug>/model-list/add_model', views.AddModel.as_view(), name='add_model'),
]