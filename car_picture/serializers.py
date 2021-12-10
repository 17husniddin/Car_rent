from rest_framework import serializers
from .models import *

class   Car_pictureSerializer(serializers.ModelSerializer):
    class Meta():
        model = Car_picture
        fields = '__all__'