from django.urls import path
from .views import (
    camera_live,
    Camera)

urlpatterns = [
    path('', Camera.as_view(), name='camera'),
    path('video_feed/', camera_live, name='camera_live'),
]
