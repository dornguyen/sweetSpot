# serializers.py
from rest_framework import serializers
from .models import Spot

class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = ['id', 'name', 'address', 'latitude', 'longitude', 'capacity']