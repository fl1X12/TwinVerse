from django.contrib import admin

# Register your models here.
from .models import PurchaseLog

admin.site.register(PurchaseLog)