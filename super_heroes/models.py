from tkinter import CASCADE
from django.db import models
from supers_types.models import SuperType
# Create your models here.

class SuperHero(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    secondary_ability = models.CharField(max_length=255)
    catch_phrase = models.CharField(max_length=255)
    super_type = models.ForeignKey(SuperType, on_delete=models.SET_NULL, null=True)

    