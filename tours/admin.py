from django.contrib import admin
from .models import Tour, Destination, Booking

# Register your models here.
admin.site.register(Tour)
admin.site.register(Destination)
admin.site.register(Booking)
