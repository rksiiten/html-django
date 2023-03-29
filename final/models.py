# import the standard Django Model
# from built-in library
from django.db import models
   
# declare a new model with a name "PersonModel"
class Person(models.Model):
  
    # fields of the model
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200)
    brand = models.CharField(max_length = 50)
  
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.name