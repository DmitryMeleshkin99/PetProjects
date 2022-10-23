from django.db import models
from django.db.models.base import Model

class Sneaker(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='sneakers/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    
