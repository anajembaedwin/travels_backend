from django.shortcuts import render
from rest_framework import viewsets
from .models import Tour, Destination, Booking
from .serializers import TourSerializer, DestinationSerializer, BookingSerializer

# Create your views here.
class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

