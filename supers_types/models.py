from tkinter import CASCADE
from django.db import models
# Create your models here.

# class Supers(models.Model):
#     name = models.CharField(max_length=255)
#     alter_ego = models.CharField(max_length=255)
#     primary_ability = models.CharField(max_length=255)
#     secondary_ability = models.CharField(max_length=255)
#     catch_phrase = models.CharField(max_length=255)
#     super_type = models.ForeignKey(SuperType, on_delete=CASCADE)

class SuperType(models.Model):
    type = models.CharField(max_length=50, null=True)
   

    
