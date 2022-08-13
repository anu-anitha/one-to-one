from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# it was to minimize data storage and provide separate security measures
#  https://www.youtube.com/watch?v=fHg3NbN6mNk

# class Place(models.Model): 

#     name = models.CharField(max_length=40) 
#     address = models.CharField(max_length=40) 

#     def __str__(self): 
#         return "%s the place" % self.name  

# class Restaurant(models.Model): 
#     place = models.OneToOneField( Place, on_delete = models.CASCADE, primary_key=True) 

#     hot_dogs = models.BooleanField(default= False) 
#     pizza = models.BooleanField(default= False) 

#     def __str__(self): 
#         return "%s the restaurant" % self.place.name 

# class Waiter(models.Model): 
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE) 
#     name = models.CharField(max_length=40) 
 
#     def __str__(self): 
#         return "%s the waiter at %s" % (self.name, self.restaurant)



#------------- another example---------------------

# https://fmhelp.filemaker.com/help/18/fmp/en/index.html#page/FMP_Help%2Fmany-to-many-relationships.html%23



class Person(models.Model):
    aadhar=models.CharField(max_length=40)
    name=models.OneToOneField( User, on_delete = models.CASCADE, related_name='p')
    def __str__(self):
        return self.aadhar


class Personn(models.Model):
    aadharr = models.CharField(max_length=40)
    namee = models.ManyToManyField(User)
