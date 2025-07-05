from django.contrib import admin
from .models import verse_post
from .models import PurchaseLog

# Register your models here.
admin.site.register(verse_post)

admin.site.register(PurchaseLog)