from django.db import models
from django.conf import settings

class TwinProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='twin_profile')
    catchphrase = models.CharField(max_length=255, blank=True, null=True)
    # Style - now allows any string input by the user
    style = models.CharField(max_length=50, blank=True, null=True) # Removed choices

    interests = models.JSONField(default=list)
    shoppingTime = models.JSONField(default=list)

    # Reaction - now allows any string input by the user
    reaction = models.CharField(max_length=50, blank=True, null=True) # Removed choices

    # Favorite Category - now allows any string input by the user
    favCategory = models.CharField(max_length=50, blank=True, null=True) # Removed choices

    avatar = models.URLField(max_length=200, blank=True, null=True)

    # Assuming this remains an IntegerField not directly from frontend input
    shopping_frequency = models.IntegerField(default=3, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.user:
            # Assuming your custom User model has a 'username' field
            return f"Profile for {self.user.username}"
        return f"TwinProfile (No User)"

    class Meta:
        verbose_name = "Twin Profile"
        verbose_name_plural = "Twin Profiles"