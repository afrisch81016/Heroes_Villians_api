from rest_framework import serializers
from .models import Heroes, Product, Villian

class Heroesserializer(serializers.ModelSerializer):
    class Meta:
        model = Heroes
        fields =['id','alter_ego','name','primary_ability','secondary_ability','catch_phrase']
