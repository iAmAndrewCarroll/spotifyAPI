from rest_framework import serializers
from .models import Spotify 

class SpotifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Spotify
        fields = ('id', 'owner', 'name', 'description', 'created_at', 'updated_at')