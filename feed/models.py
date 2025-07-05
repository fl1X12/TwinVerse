from django.db import models
from django.conf import settings

class PurchaseLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='purchases')
    item_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    purchased_at = models.DateTimeField(auto_now_add=True)
    private = models.BooleanField(default=False)  # Private purchase flag

    def __str__(self):
        return f"{self.user.username} bought {self.item_name} for {self.amount}"