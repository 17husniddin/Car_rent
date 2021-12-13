from .models import *
from .serializers import *
from rest_framework import viewsets

class Car_dateViewSet(viewsets.ModelViewSet):
    queryset = Car_date.objects.all()
    serializer_class = Car_dateSerializer