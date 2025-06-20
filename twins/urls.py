from django.urls import path
from .views import TwinProfileView

urlpatterns = [
    path('profile/', TwinProfileView.as_view(), name='twin-profile'),
]
