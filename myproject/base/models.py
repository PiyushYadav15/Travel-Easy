from django.db import models

# Create your models here.
from django.contrib.auth.models import User
#type 
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self): # to increase the code Readability
        return self.name
#destination 
class Destination(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_deleted=models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.name
    


class Guide(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='guides')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name


