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
    path('brands/', views.BrandList.as_view(), name='brand_list'),
    path('add-brand/', views.AddBrand.as_view(), name='add_brand'),
    path('edit/<slug:brand_slug>/', views.UpdateBrand.as_view(), name='edit_brand'),
    path('brands/<slug:brand_slug>/', views.ModelList.as_view(), name='model_list'),
    path('brands/<slug:brand_slug>/add-model/', views.AddModel.as_view(), name='add_model'),
    path('brands/<slug:brand_slug>/edit-model/<slug:model_slug>/', views.UpdateModel.as_view(), name='edit_model'),
    path('brands/<slug:brand_slug>/<slug:model_slug>/', views.GenList.as_view(), name='gen_list'),
    path('brands/<slug:brand_slug>/<slug:model_slug>/add-gen/', views.AddGen.as_view(), name='add_gen'),
    path('brands/<slug:brand_slug>/<slug:model_slug>/edit-gen/<slug:gen_slug>', views.UpdateGen.as_view(), name='edit_gen')
]