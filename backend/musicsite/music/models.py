from django.db import models
from django.conf import settings

# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='music_posts')
    file = models.FileField(upload_to='music/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class MusicianProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='musician_profiles/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username