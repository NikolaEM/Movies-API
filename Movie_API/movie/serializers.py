from rest_framework import serializers
from .models import Genre, Movie, Comment

class MovieSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_dislikes_count(self, obj):
        return obj.dislikes.count()

    class Meta:
        depth = 1
        model = Movie
        fields = (
            "likes_count",
            "dislikes_count",
            "title",
            "description",
            "movie_cover",
            "user",
            "genre",
            "id",
            'number_of_views',
            )   

class CreateMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('__all__')

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
            model = Genre
            fields = ('__all__')    

class RetrieveMovieSerializer(BaseException):
    def retrieve(self, instance):
        instance.number_of_views += 1
        instance.save()
        return instance

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'movie']