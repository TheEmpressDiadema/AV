from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car, Brand
from django.urls import reverse_lazy
# Create your views here.
class BrandList(ListView):
    model = Brand
    template_name = 'carshop/brand_list.html'
    context_object_name = 'brands'

class AddBrand(CreateView):
    model = Brand
    template_name = 'carshop/add_brand.html'
    fields = ['name']
    success_url = reverse_lazy('home')