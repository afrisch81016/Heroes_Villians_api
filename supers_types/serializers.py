from rest_framework import serializers
from .models import SuperType

# class Heroesserializer(serializers.ModelSerializer):
#     class Meta:
#         super_type = Supers
#         fields =['id','alter_ego','name','primary_ability','secondary_ability','catch_phrase', 'super_type']

class SuperTypeserializers(serializers.ModelSerializer):
    class Meta :
        model = SuperType
        fields = ['id','type']
        depth = 1
