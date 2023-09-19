from django.contrib import admin
from .models import Tour, Destination, Booking

class DestinationInline(admin.TabularInline):
    model = Destination

class TourAdmin(admin.ModelAdmin):
    inlines = [DestinationInline]

# Register your models here.
admin.site.register(Tour, TourAdmin)
admin.site.register(Destination)
admin.site.register(Booking)
