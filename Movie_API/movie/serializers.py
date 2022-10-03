from rest_framework import serializers
from .models import Genre, Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('__all__')

class CreateMovieSerializer(serializers.ModelSerializer):

    def create(self, data):
        return Movie.objects.create(**data)

    class Meta:
        model = Movie
        fields = ('__all__')

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
            model = Genre
            fields = ('__all__')    