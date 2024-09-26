from rest_framework import serializers

from watchlist_app.models import Movies


"""
There are two types of serializers:

1. ModelSerializer
2. Serializer
Here we are using  Serializer  itself.
so the rendering is different , for modelserializer is been done as model form in django forms
"""
class MoviesSerializer(serializers.Serializer):
    class Meta:
        
        id = serializers.IntegerField(read_only=True)
        title = serializers.CharField()
        description = serializers.CharField()
        active = serializers.BooleanField()