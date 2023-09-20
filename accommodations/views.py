from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Accommodation
from .serializers import AccommodationSerializer

# Create your views here.
@api_view(['GET'])
def accommodation_list(request):
    accommodations = Accommodation.objects.all()
    serializer = AccommodationSerializer(accommodations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def accommodation_detail(request, accommodation_id):
    accommodation = get_object_or_404(Accommodation, pk=accommodation_id)
    serializer = AccommodationSerializer(accommodation)
    return Response(serializer.data)
