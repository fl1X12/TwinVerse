from django.db import models
from django.conf import settings

# Create your models here.
class TwinProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='twin_profile')

    shopping_priorities=models.JSONField(default=list)
    interests=models.JSONField(default=list)
    brand_affinities=models.JSONField(default=list)
    price_sensitivity=models.JSONField(default=list)
    shopping_frequency=models.CharField(default=3)
    vibe=models.JSONField(default=list)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.name}"