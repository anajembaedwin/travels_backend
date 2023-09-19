from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TourViewSet, DestinationViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'tours', TourViewSet, basename='tour')
router.register(r'destinations', DestinationViewSet, basename='destination')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('', include(router.urls)),
]
