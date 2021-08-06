from django.db import models
from django.core.validators import MaxLengthValidator


# Create your models here.

class Warranty(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    number_of_products = models.PositiveIntegerField(default=1, validators=[MaxLengthValidator(10)])
