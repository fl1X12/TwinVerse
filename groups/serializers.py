from rest_framework import serializers
from .models import Group

class GroupSerializer(serializers.ModelSerializer):
    admin_name = serializers.CharField(source="admin.username", read_only=True)
    members = serializers.SlugRelatedField(many=True, slug_field="username", read_only=True)

    class Meta:
        model = Group
        fields = ["id", "name", "icon", "admin", "admin_name", "members", "created_at"]
        read_only_fields = ["admin", "admin_name", "created_at", "members"]