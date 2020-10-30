from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Breed(models.Model):
    TINY = 'Tiny'
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'Large'
    SIZES = [
        (TINY, 'Tiny')
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    ]

    name = models.CharField(max_length=30)
    size = models.CharField(max_length=6, choices=SIZES, default=TINY)
    friendliness = models.IntegerField(default=1, validators=[MinValueValidator(min_value=1), MaxValueValidator(max_value=5)])
    trainability = models.IntegerField(default=1, validators=[MinValueValidator(min_value=1), MaxValueValidator(max_value=5)])
    sheddingamount = models.IntegerField(default=1, validators=[MinValueValidator(min_value=1), MaxValueValidator(max_value=5)])
    exerciseneeds = models.IntegerField(default=1, validators=[MinValueValidator(min_value=1), MaxValueValidator(max_value=5)])

class Dog(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1)
    color = models.CharField(max_length=30)
    favoritefood = models.CharField(max_length=30)
    favoritetoy = models.CharField(max_length=30)
