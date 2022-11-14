from django.contrib import admin
from advertisements.models import Advertisement


# Register your models here.

@admin.register(Advertisement)
class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'creator', 'title', 'description', 'created_at')
