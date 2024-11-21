from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('add-engine/', views.CreateEngine.as_view(), name='add_engine'),
    path('brands/', views.BrandList.as_view(), name='brand_list'),
    path('add-brand/', views.AddBrand.as_view(), name='add_brand'),
    path('edit/<slug:brand_slug>/', views.UpdateBrand.as_view(), name='edit_brand'),
    path('brands/<slug:brand_slug>/', views.ModelList.as_view(), name='model_list'),
    path('brands/<slug:brand_slug>/add-model/', views.AddModel.as_view(), name='add_model'),
    path('brands/<slug:brand_slug>/edit-model/<slug:model_slug>/', views.UpdateModel.as_view(), name='edit_model'),
    path('brands/<slug:brand_slug>/<slug:model_slug>/', views.GenList.as_view(), name='gen_list'),
    path('brands/<slug:brand_slug>/<slug:model_slug>/add-gen/', views.AddGen.as_view(), name='add_gen'),
    path('brands/<slug:brand_slug>/<slug:model_slug>/edit-gen/<slug:gen_slug>', views.UpdateGen.as_view(), name='edit_gen'),
    path('brands/<slug:brand_slug>/<slug:model_slug>/<slug:gen_slug>/', views.CarList.as_view(), name='car_list'),
    path('brands/<slug:brand_slug>/<slug:model_slug>/<slug:gen_slug>/add-car/', views.CreateCar.as_view(), name='add_car'),
    path('brands/<slug:brand_slug>/<slug:model_slug>/<slug:gen_slug>/edit-car/<slug:car_slug>/', views.UpdateCar.as_view(), name="edit_car"),
    path('brands/<slug:brand_slug>/<slug:model_slug>/<slug:gen_slug>/<slug:car_slug>/', views.CarView.as_view(), name="car")
]