from rest_framework import serializers
from .models import SuperHero

class SuperHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperHero
        fields =['id','alter_ego','name','primary_ability','secondary_ability','catch_phrase', 'super_type','super_type_id']
        depth = 1
    super_type_id = serializers.IntegerField(write_only = True)
