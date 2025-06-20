from rest_framework import serializers
from .models import TwinProfile

class TwinProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwinProfile
        fields = '__all__'
        read_only_fields = ['user']
