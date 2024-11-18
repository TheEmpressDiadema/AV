from django import forms
from django.forms import inlineformset_factory
from .models import Car, CarImage

class CarImageForm(forms.ModelForm):
    class Meta:
        model = CarImage
        fields = ['image']

car_image_formset = inlineformset_factory(Car, CarImage, form=CarImageForm, extra=1, can_delete=True)