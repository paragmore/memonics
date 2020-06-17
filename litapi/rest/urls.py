from django.urls import path
from litapi.rest import views

urlpatterns = [
    path('lit/', views.api_video_view,),
    path('lit/channel/<int:slug>/', views.api_channel_video_view, name='channel-detail'),
]