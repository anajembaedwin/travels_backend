from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Destination
from .serializers import DestinationSerializer

@api_view(['GET'])
def destination_list(request):
    destinations = Destination.objects.all()
    serializer = DestinationSerializer(destinations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def destination_detail(request, destination_id):
    try:
        destination = Destination.objects.get(pk=destination_id)
        serializer = DestinationSerializer(destination)
        return Response(serializer.data)
    except Destination.DoesNotExist:
        return Response({'message': 'Destination not found'}, status=404)
