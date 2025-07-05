from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from .views import PublicPurchaseFeed, CreatePurchaseLog, LeaderboardView,  CelebTwinsView

urlpatterns = [
    path('public-feed/', PublicPurchaseFeed.as_view(), name='public-purchase-feed'),
    path('purchase/', CreatePurchaseLog.as_view(), name='create-purchase-log'),
    path('admin/', admin.site.urls),
    #path('feed/', include('feed.urls')),
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
    # path('profile/', TwinProfileView.as_view(), name='twin-profile'),
    path('celeb-twins/', CelebTwinsView.as_view(), name='celeb-twins'),
]