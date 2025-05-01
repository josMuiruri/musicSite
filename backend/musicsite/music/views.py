from rest_framework import viewsets
from . models import Music, Comment, MusicianProfile
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
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        music_id = self.kwargs.get('pk')
        music = Music.objects.get(pk=music_id)
        serializer.save(user=self.request.user, music=music)
        return super().perform_create(serializer)