from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.decorators import action
from movie.pagination import CustomPageNumberPagination
from .models import Movie, Genre
from .serializers import CreateMovieSerializer, GenreSerializer, MovieSerializer

class MovieViewSet(RetrieveModelMixin, GenericViewSet, CreateModelMixin, ListModelMixin):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = CustomPageNumberPagination
    search_fields = ['title'] 
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['genre'] 
    

    def create(self, request):
        data = request.data.copy() 
        data["movie_cover"] = request.FILES.get("movie_cover")
        data["user"] = request.user.id
        serializer = CreateMovieSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        response = serializer.save()
           
        return Response(MovieSerializer(response, context={'request': request}).data, HTTP_201_CREATED)

    @action(detail=True, methods=["patch"], url_path='likes', permission_classes=[IsAuthenticated])
    def like_movie(self, request, pk):
        return Response(MovieSerializer(Movie.like_movie(request.user, pk), context={'request': request}).data)

    @action(detail=True, methods=["patch"], url_path='dislikes', permission_classes=[IsAuthenticated])
    def dislike_movie(self, request, pk):
        return Response(MovieSerializer(Movie.dislike_movie(request.user, pk), context={'request': request}).data)

class GenreViewSet(GenericViewSet, ListModelMixin):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated]
