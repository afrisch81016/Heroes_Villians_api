from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from supers_types.serializers import Heroesserializer
from .models import Supers

# Create your views here.
@api_view(['GET'])
def super_heroes_types(request):

    super_param = request.query.params.get('supers')
    


@api_view(['GET','POST'])
def superheroes(request,):

    if request.method == 'GET':
        supers = Supers.objects.all()
        serializer = Heroesserializer(supers,many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Heroesserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (serializer.data,status = status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def superheroes_detail(request,pk):
    supers_details = get_object_or_404(Supers,pk=pk)

    if request.method == 'GET':
        serializer = Heroesserializer(supers_details)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Heroesserializer(supers_details,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
    elif request.method == 'DELETE':
        supers_details.delete()

        return Response (status = status.HTTP_204_NO_CONTENT)


