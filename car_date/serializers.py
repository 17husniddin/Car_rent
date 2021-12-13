from rest_framework import serializers
from .models import *

class   Car_dateSerializer(serializers.ModelSerializer):
    class Meta():
        model = Car_date
        fields = '__all__'