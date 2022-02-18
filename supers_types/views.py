from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SuperType
from .serializers import SuperTypeserializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def super_types_list(request):
    if request.method == 'GET':
        supers_types = SuperType.objects.all()
        serializer = SuperTypeserializers(supers_types, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuperTypeserializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

