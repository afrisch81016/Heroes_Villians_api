from django.db import models
# Create your models here.

class SuperType (models.Model):
    type = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.type
   

    
