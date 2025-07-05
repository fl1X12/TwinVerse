from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import status
from users.models import CustomUser
from feed.models import PurchaseLog
from django.db.models import Count
from .serializers import PurchaseLogSerializer

class PublicPurchaseFeed(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        purchases = PurchaseLog.objects.filter(private=False).order_by('-purchased_at')
        serializer = PurchaseLogSerializer(purchases, many=True)
        return Response(serializer.data)

class CreatePurchaseLog(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PurchaseLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeaderboardView(APIView):
    """
    Returns a leaderboard of users ranked by number of purchases.
    """
    def get(self, request):
        leaderboard = (
            CustomUser.objects.annotate(purchase_count=Count('purchases'))
            .order_by('-purchase_count', 'username')
            .values('username', 'purchase_count')[:10]
        )
        return Response(list(leaderboard))

class CelebTwinsView(APIView):
    """
    Returns static celeb twin data.
    """
    def get(self, request):
        celeb_twins = [
            {"name": "Taylor Swift", "traits": ["music", "fashion", "pop culture"]},
            {"name": "Cristiano Ronaldo", "traits": ["sports", "fitness", "luxury"]},
            {"name": "Oprah Winfrey", "traits": ["media", "inspiration", "books"]},
            # Add more static celeb twins as needed
        ]
        return Response(celeb_twins)