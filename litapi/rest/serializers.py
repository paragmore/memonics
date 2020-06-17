from rest_framework import serializers

from litapi.models import Video, Channel

class VideoSerializer(serializers.ModelSerializer):
    channel_id= serializers.PrimaryKeyRelatedField(queryset=Channel.objects.all(),source='channel.channelName')
    class Meta:
        model = Video
        fields = ['id', 'videoId', 'caption', 'channel_id']

class ChannelVideoSerializer(serializers.ModelSerializer):
    videos= VideoSerializer(many=True)

    class Meta:
        model = Channel
        fields = ['id', 'channelName', 'videos']