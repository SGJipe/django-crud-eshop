from django import forms
from django.forms import ModelForm
from .models import Question

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ('text', 'date')
        labels = {
            'text': '',
            'date' : ''
        }
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What is your question ?'}),
            'date': forms.DateTimeInput(format=('%d/%m/%Y %H:%M:%S'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }