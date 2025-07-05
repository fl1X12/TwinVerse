from django.db import models
from django.conf import settings

# Create your models here.
class verse_post(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    caption=models.TextField(max_length=150)
    image=models.ImageField(upload_to='verse_images/')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
