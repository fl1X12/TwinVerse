from rest_framework import serializers
from .models import PurchaseLog,VersePost, PostReaction, PostComment

class PurchaseLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseLog
        fields = ['id', 'user', 'item_name', 'amount', 'purchased_at', 'private']
        read_only_fields = ['user', 'purchased_at']

from django.contrib.auth import get_user_model
User = get_user_model()

class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PostCommentSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=VersePost.objects.all(), write_only=True)

    class Meta:
        model = PostComment
        fields = ['id', 'user', 'post', 'comment', 'created_at']
        read_only_fields = ['user', 'created_at']

class PostReactionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=VersePost.objects.all(), write_only=True)

    class Meta:
        model = PostReaction
        fields = ['id', 'user', 'post', 'type', 'created_at']
        read_only_fields = ['user', 'created_at']



class VersePostSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    reactions = PostReactionSerializer(many=True, read_only=True)
    comments = PostCommentSerializer(many=True, read_only=True)
    reaction_count = serializers.ReadOnlyField()
    comment_count = serializers.ReadOnlyField()

    class Meta:
        model = VersePost
        fields = [
            'id', 'user', 'caption', 'image',
            'created_at', 'updated_at',
            'reactions', 'comments',
            'reaction_count', 'comment_count'
        ]
    def get_user(self, obj):
        return {
            "username": obj.user.username,
        }