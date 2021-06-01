from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Tasca(models.Model):
      name = models.CharField(max_length=100)
      address = models.CharField(max_length=200)
      rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
