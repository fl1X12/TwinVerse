from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import VersePostViewSet,PostReactionViewSet,PostCommentViewSet,PublicPurchaseFeed, CreatePurchaseLog, LeaderboardView,  CelebTwinsView

router = DefaultRouter()
router.register(r'posts', VersePostViewSet, basename='posts')
router.register(r'reactions', PostReactionViewSet, basename='reactions')
router.register(r'comments', PostCommentViewSet, basename='comments')

urlpatterns = [
    path('public-feed/', PublicPurchaseFeed.as_view(), name='public-purchase-feed'),
    path('purchase/', CreatePurchaseLog.as_view(), name='create-purchase-log'),
    path('admin/', admin.site.urls),
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
    path('celeb-twins/', CelebTwinsView.as_view(), name='celeb-twins'),
]

urlpatterns += router.urls