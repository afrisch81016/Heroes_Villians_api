from ast import Or
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from supers_types.models import SuperType
from .serializers import SuperHeroSerializer
from .models import SuperHero

# Create your views here.


@api_view(['GET','POST'])
def supers_list(request):

    if request.method == 'GET':
        supers = SuperHero.objects.all()
        serializer = SuperHeroSerializer(supers,many = True)

        heroes = supers.filter(super_type__type='Hero')
        villains = supers.filter(super_type__type='Villian')

        hero_serializer = SuperHeroSerializer(heroes, many = True)
        villain_serializer = SuperHeroSerializer(villains, many = True)

        if request.query_params.get('type') == 'hero':
            #returns all heros 
            response = hero_serializer.data
            return Response(response)
        elif request.query_params.get('type') == 'villain':
            #returns all villains 
            response = villain_serializer.data
            return Response(response)
        else:
            return Response(serializer.data)
 

    elif request.method == 'POST':
        serializer = SuperHeroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (serializer.data, status = status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def superheroes_detail(request,pk):
    supers_details = get_object_or_404(SuperHero,pk=pk)

    if request.method == 'GET':
        serializer = SuperHeroSerializer(supers_details)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SuperHeroSerializer(supers_details,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
    elif request.method == 'DELETE':
        supers_details.delete()

        return Response (status = status.HTTP_204_NO_CONTENT)



  