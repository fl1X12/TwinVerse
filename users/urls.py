from django.urls import path
from .views import RegisterView, ProfileView,FollowUserView,DiscoverProfilesView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('me/', ProfileView.as_view()),
    path('follow/', FollowUserView.as_view(),name='follow_unfollow'),
    path('discover/', DiscoverProfilesView.as_view(), name='discover_profiles'),
]
