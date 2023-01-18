from django.shortcuts import render
from core.models import PropertyType
# Create your views here.
from .seriallaizers import PropertyTypeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def property_type_list(request):
    if request.method == 'GET':
        property_types = PropertyType.objects.all()
        serializer = PropertyTypeSerializer(property_types, many=True)
        return Response(serializer.data)
    return Response(serializer.data)