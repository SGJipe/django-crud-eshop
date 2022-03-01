from django.contrib import admin
from .models import Pokemon

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fields = ['date', 'text']

admin.site.register(Pokemon)