from rest_framework import serializers
from .models import CustomUser,Profile

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'name','username', 'password']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    name = serializers.CharField(source="user.name")
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ["id", "username", "name", "avatar"]

    def get_avatar(self, obj):
        # This safely handles cases where TwinProfile may not be linked
        twin = getattr(obj.user, 'twin_profile', None)
        return twin.avatar if twin and twin.avatar else None


class FollowUserSerializer(serializers.Serializer):
    target_username=serializers.CharField()

    def validate_target_username(self, value):
        try:
            user=CustomUser.objects.get(username=value)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("User with this username does not exist.")
        return value

class DiscoverProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    name = serializers.CharField(source='user.name')

    class Meta:
        model = Profile
        fields = ['id', 'username', 'name']