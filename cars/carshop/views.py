from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Brand, CarModel, Gen, Engine, Car
from django.urls import reverse_lazy
# Create your views here.
class IndexView(TemplateView):
    '''
    '''
    template_name = 'carshop/index.html'

class BrandList(ListView):
    '''
    '''
    model = Brand
    template_name = 'carshop/brand_list.html'
    context_object_name = 'brands'
    extra_context = {
        'add_brand_link' : "add_brand"
    }

class AddBrand(CreateView):
    '''
    '''
    model = Brand
    template_name = 'carshop/add_brand.html'
    fields = ['name']
    success_url = reverse_lazy('brand_list')
    extra_context = {
        'view_name' : "add"
    }
    
class UpdateBrand(UpdateView):
    '''
    '''
    model = Brand
    template_name = 'carshop/add_brand.html'
    fields = ['name']
    success_url = reverse_lazy('brand_list')
    slug_url_kwarg = 'brand_slug'
    extra_context = {
        'view_name' : "edit"
    }

class ModelList(ListView):
    '''
    '''
    model = CarModel
    template_name = 'carshop/model_list.html'
    context_object_name = 'car_models'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_model_link'] = reverse_lazy('add_model', kwargs={'brand_slug' : self.kwargs['brand_slug']})
        context['brand'] = Brand.objects.get(slug=self.kwargs['brand_slug'])
        return context

    def get_queryset(self):
        return CarModel.objects.filter(brand__slug=self.kwargs['brand_slug'])

class AddModel(CreateView):
    '''
    '''
    model = CarModel
    template_name = 'carshop/add_model.html'
    fields = ['name']

    def form_valid(self, form):
        brand = get_object_or_404(Brand, slug=self.kwargs['brand_slug'])
        form.instance.brand = brand
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse_lazy('model_list', kwargs={'brand_slug' : self.kwargs['brand_slug']})


class UpdateModel(UpdateView):
    '''
    '''
    model = CarModel
    template_name = 'carshop/add_model.html'
    fields = ['name']

    def get_object(self, queryset=None):
        return get_object_or_404(CarModel, brand__slug=self.kwargs['brand_slug'], slug=self.kwargs['model_slug'])

    def form_valid(self, form):
        brand = get_object_or_404(Brand, slug=self.kwargs['brand_slug'])
        form.instance.brand = brand
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('model_list', kwargs={'brand_slug' : self.kwargs['brand_slug']})


class GenList(ListView):
    '''
    
    '''
    model = Gen
    template_name = 'carshop/gen_list.html'
    context_object_name = 'generations'
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_gen_link'] = reverse_lazy('add_gen', kwargs={
            'brand_slug' : self.kwargs['brand_slug'], 
            'model_slug' : self.kwargs['model_slug']
            }
            )
        context['brand'] = Brand.objects.get(slug=self.kwargs['brand_slug'])
        context['model'] = CarModel.objects.get(slug=self.kwargs['model_slug'])
        return context
    
    def get_queryset(self):
        return Gen.objects.filter(model__slug=self.kwargs['model_slug'])
    
class AddGen(CreateView):
    '''
    
    '''
    model = Gen
    template_name = 'carshop/add_gen.html'
    fields = ['name', 'image', 'release_start', 'release_end']


    def form_valid(self, form):
        model = get_object_or_404(CarModel, slug=self.kwargs['model_slug'])
        form.instance.model = model
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse_lazy('gen_list', kwargs={
            'brand_slug' : self.kwargs['brand_slug'], 
            'model_slug' : self.kwargs['model_slug']
            }
            )
    
class UpdateGen(UpdateView):
    '''
    
    '''
    model = Gen
    template_name = 'carshop/add_gen.html'
    fields = ['name', 'image', 'release_start', 'release_end']

    def get_object(self, queryset=None):
        return get_object_or_404(Gen, slug=self.kwargs['gen_slug'])

    def form_valid(self, form):
        model = get_object_or_404(CarModel, slug=self.kwargs['model_slug'])
        form.instance.model = model
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse_lazy('gen_list', kwargs={
            'brand_slug' : self.kwargs['brand_slug'], 
            'model_slug' : self.kwargs['model_slug']
            }
            )
    
class CreateEngine(CreateView):
    model = Engine
    template_name = "carshop/add_engine.html"
    fields = ['name', 'fuel_type', 'volume', 'power', 'milage']
    success_url = reverse_lazy('home')

class CarList(ListView):
    model = Car
    template_name = 'carshop/car_list.html'
    context_object_name = 'cars'
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_car_link'] = reverse_lazy('add_car', kwargs={
            'gen_slug' : self.kwargs['gen_slug'],
            'brand_slug' : self.kwargs['brand_slug'], 
            'model_slug' : self.kwargs['model_slug']
            }
            )
        context['brand'] = Brand.objects.get(slug=self.kwargs['brand_slug'])
        context['model'] = CarModel.objects.get(slug=self.kwargs['model_slug'])
        context['gen'] = Gen.objects.get(slug=self.kwargs['gen_slug'])
        return context
    
    def get_queryset(self):
        return Car.objects.filter(gen__slug=self.kwargs['gen_slug'])
    
class CreateCar(CreateView):
    model = Car
    template_name = 'carshop/add_gen.html'
    fields = ['engine', 'vin', 'color', 'description']


    def form_valid(self, form):
        gen = get_object_or_404(Gen, slug=self.kwargs['gen_slug'])
        form.instance.gen = gen
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse_lazy('gen_list', kwargs={
            'gen_slug' : self.kwargs['gen_slug'],
            'brand_slug' : self.kwargs['brand_slug'], 
            'model_slug' : self.kwargs['model_slug']
            }
            )
    
class UpdateCar(UpdateView):
    model = Car
    template_name = 'carshop/add_gen.html'
    fields = ['engine', 'vin', 'color', 'description']

    def get_object(self, queryset=None):
        return get_object_or_404(Car, slug=self.kwargs['car_slug'])

    def form_valid(self, form):
        gen = get_object_or_404(Gen, slug=self.kwargs['gen_slug'])
        form.instance.model = gen
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse_lazy('gen_list', kwargs={
            'gen_slug' : self.kwargs['gen_slug'],
            'brand_slug' : self.kwargs['brand_slug'], 
            'model_slug' : self.kwargs['model_slug']
            }
            )
