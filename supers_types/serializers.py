from rest_framework import serializers
from .models import Heroes, Product, SuperType, Villian

# class Heroesserializer(serializers.ModelSerializer):
#     class Meta:
#         super_type = Supers
#         fields =['id','alter_ego','name','primary_ability','secondary_ability','catch_phrase', 'super_type']

class SuperType(serializers.ModelSerializer):
    class Meta :
        model = SuperType
        fields = ['id','type']
