from rest_framework import serializers
from . models import Music, Comment, MusicianProfile

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at']

class MusicSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Music
        fields = '__all__'

class MusicianProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.name', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = MusicianProfile
        fields = '__all__'