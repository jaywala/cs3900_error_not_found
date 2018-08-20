from django.contrib import admin

from .models import Advertisement

# Register your models here.

class AdvertismentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,    {'fields': ['accommodation_name']}),
        ('Price', {'fields': ['base_price']}),
    ]

admin.site.register(Advertisement, AdvertismentAdmin)
