from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from litapi.models import Video, Channel
from litapi.rest.serializers import VideoSerializer,ChannelVideoSerializer

@api_view(['GET',])

def api_video_view(request):
    if request.method == 'GET':
        videos = Video.objects.all()
        
        serializer = VideoSerializer(videos,context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def api_channel_video_view(request,slug):
    if request.method == 'GET':
        videos = Channel.objects.filter(id=slug)
        serializer = ChannelVideoSerializer(videos, many=True)
        return Response(serializer.data)






