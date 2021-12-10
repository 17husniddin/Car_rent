from django.shortcuts import render
from car_picture.models import *
from .serializers import *
from rest_framework import viewsets

class Car_pictureViewSet(viewsets.ModelViewSet):
    queryset = Car_picture.objects.all()
    serializer_class = Car_pictureSerializer