from django.urls import path
from .views import SpotifyList, SpotifyDetail

urlpatterns = [
    path("", SpotifyList.as_view(), name="home"),
    path('<int:pk>', SpotifyDetail.as_view(), name='spotify_detail'),
]