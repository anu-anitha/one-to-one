from django.db import models

# Create your models here.

class Place(models.Model): 

    name = models.CharField(max_length=40) 
    address = models.CharField(max_length=40) 

    def __str__(self): 
        return "%s the place" % self.name  

class Restaurant(models.Model): 
    place = models.OneToOneField( Place, on_delete = models.CASCADE, primary_key=True) 

    hot_dogs = models.BooleanField(default= False) 
    pizza = models.BooleanField(default= False) 

    def __str__(self): 
        return "%s the restaurant" % self.place.name 

class Waiter(models.Model): 
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE) 
    name = models.CharField(max_length=40) 
 
    def __str__(self): 
        return "%s the waiter at %s" % (self.name, self.restaurant)
