from django import forms
from django.forms import inlineformset_factory, BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Car

class CarForm(forms.ModelForm):
    images = forms.ImageField(
        required=False,
        label="Фотографии"
    )

    class Meta:
        model = Car
        fields = ['engine', 'vin', 'color', 'milage', 'price', 'description']