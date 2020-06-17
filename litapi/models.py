from django.db import models

# Create your models here.

class Channel(models.Model):
    channelName= models.CharField(max_length=100)
    
    def __str__(self):
        return self.channelName

class Video(models.Model):
    videoId= models.CharField(max_length=200)
    caption= models.TextField(max_length=300)
    channel= models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='videos')

    def __str__(self):
        return self.caption
    


