from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Activity
from .serializers import ActivitySerializer

@api_view(['GET'])
def activity_list(request):
    activities = Activity.objects.all()
    serializer = ActivitySerializer(activities, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def activity_detail(request, activity_id):
    try:
        activity = Activity.objects.get(pk=activity_id)
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)
    except Activity.DoesNotExist:
        return Response({'message': 'Activity not found'}, status=404)
