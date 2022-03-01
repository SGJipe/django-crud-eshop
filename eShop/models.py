from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Pokemon(models.Model):
    MALE = 'ML'
    FEMALE = 'FM'
    GENDER = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    level = models.IntegerField(default=1, validators=[MaxValueValidator(100)])
    shiny = models.BooleanField()
    gender = models.CharField(max_length=10, choices=GENDER)
    picture = models.ImageField(null=True, blank=True, upload_to="img/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

    def read_gender(self):
        GENDER = {
            'ML' : 'Male',
            'FM' : 'Female'
        }
        return GENDER.get(self.gender)
