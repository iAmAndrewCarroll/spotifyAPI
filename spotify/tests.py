from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Spotify

class SpotifyTests(TestCase):
    @classmethod
    def setUpTEstData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_spotify = Spotify.objects.create(name=)

# Create your tests here.
