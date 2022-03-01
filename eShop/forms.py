from email.policy import default
from django import forms
from django.forms import ModelForm, Form
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Pokemon

class PokemonQuantityForm(ModelForm):
    class Meta:
        model = Pokemon
        fields = ('quantity',)
        labels = {
            'quantity': '',
        }
        widgets = {
            # 'quantity': forms.IntegerField(MinValueValidator(1), MaxValueValidator(model.quantity))
            'quantity': forms.NumberInput(attrs={'min': 0})
        }

class PokemonQtyForm(Form):
    quantity = forms.IntegerField(initial=1)