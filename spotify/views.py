from rest_framework import generics
from .serializer import SpotifySerializer
from .models import Spotify

class SpotifyList(generics.ListCreateAPIView):
    queryset = Spotify.objects.all()
    serializer_class = SpotifySerializer

class SpotifyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Spotify.objects.all()
    serializer_class = SpotifySerializer

    