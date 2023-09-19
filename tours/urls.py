from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TourViewSet, DestinationViewSet, BookingViewSet
# from django.contrib import admin

router_user = DefaultRouter()
router_user.register(r'tours', TourViewSet, basename='tour')
router_user.register(r'destinations', DestinationViewSet, basename='destination')
router_user.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('user/', include(router_user.urls)),
    # path('admin/', admin.site.urls),  # Default admin URLs
]

