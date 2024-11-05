from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car, Brand, CarModel
from django.urls import reverse_lazy
# Create your views here.
class IndexView(TemplateView):
    template_name = 'carshop/index.html'

class BrandList(ListView):
    model = Brand
    template_name = 'carshop/brand_list.html'
    context_object_name = 'brands'
    extra_context = {
        'add_brand_link' : "add_brand"
    }

class AddBrand(CreateView):
    model = Brand
    template_name = 'carshop/add_brand.html'
    fields = ['name']
    success_url = reverse_lazy('brand_list')
    extra_context = {
        'view_name' : "add"
    }
    
class UpdateBrand(UpdateView):
    model = Brand
    template_name = 'carshop/add_brand.html'
    fields = ['name']
    success_url = reverse_lazy('brand_list')
    slug_url_kwarg = 'brand_slug'
    extra_context = {
        'view_name' : "edit"
    }

class ModelList(ListView):
    model = CarModel
    template_name = 'carshop/model_list.html'
    context_object_name = 'car_models'
    extra_context = {
        'add_model_link' : "add_model"
    }

class AddModel(CreateView):
    model = CarModel
    template_name = 'carshop/add_model.html'
    fields = ['name', 'brand']
    success_url = reverse_lazy('model_list')
