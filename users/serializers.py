from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'name','username', 'password']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class FollowUserSerializer(serializers.Serializer):
    target_username=serializers.CharField()

    def validate_target_username(self, value):
        try:
            user=CustomUser.objects.get(username=value)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("User with this username does not exist.")
        return value