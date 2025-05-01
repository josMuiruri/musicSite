from rest_framework import viewsets
from . models import Music, MusicianProfile
from . serializers import *

# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == 'user':
            return Music.objects.filter()
        return Music.objects.all()