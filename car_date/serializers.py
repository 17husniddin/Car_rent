from rest_framework import serializers
from .models import *

class   Car_dateSerializer(serializers.ModelSerializer):
    class Meta():
        model = Car_date
        fields = '__all__'


class Car_dateReservationSerializer(serializers.Serializer):
    car = Car_dateSerializer()
    current_active_bookings = Car_dateSerializer(many=True)