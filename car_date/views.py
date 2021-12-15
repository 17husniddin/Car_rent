from .models import *
from .serializers import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

class Car_dateViewSet(viewsets.ModelViewSet):
    queryset = Car_date.objects.all()
    serializer_class = Car_dateSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['time_from','time_to']
    search_fields = ['time_from','time_to']
    ordering_fields = ['date']
    ordering = ['-id']
