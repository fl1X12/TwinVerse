from django.contrib import admin
from .models import VersePost
from .models import PurchaseLog

# Register your models here.
admin.site.register(VersePost)

admin.site.register(PurchaseLog)