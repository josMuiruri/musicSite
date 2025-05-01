from rest_framework import serializers
from . models import Music, MusicianProfile

class MusicSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Music
        fields = '__all__'

class MusicianProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.name', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    
    class Meta:
        model = MusicianProfile
        fields = '__all__'