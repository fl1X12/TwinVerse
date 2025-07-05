from rest_framework import serializers
from .models import PurchaseLog

class PurchaseLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseLog
        fields = ['id', 'user', 'item_name', 'amount', 'purchased_at', 'private']
        read_only_fields = ['user', 'purchased_at']