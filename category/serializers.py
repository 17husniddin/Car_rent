from rest_framework import serializers
from .models import *


class CarSerializer(serializers.ModelSerializer):
    class Meta():
        model = Car
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    news = CarSerializer(read_only=True, many=True)

    class Meta():
        model = Category
        fields = '__all__'