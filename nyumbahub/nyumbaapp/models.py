from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length =50)
    phone= models.CharField(max_length =50)
    email = models.EmailField()
    password = models.CharField(max_length =50)

    def __str__(self):
        return self.name

class House1(models.Model):
    title = models.CharField(max_length =50)
    description = models.TextField()
    price = models.CharField(max_length =50)
    size = models.CharField(max_length =50)
    location = models.CharField(max_length =50)
    amenities = models.TextField()
    featured_image = models.ImageField(upload_to = 'house_images/')

    def __str__(self):
        return self.title




# Create your models here.
