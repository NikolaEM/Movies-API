from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from .models import Movie, Genre
from .serializers import CreateMovieSerializer, GenreSerializer, MovieSerializer

class MovieViewSet(RetrieveModelMixin, GenericViewSet, CreateModelMixin):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request):
        data = request.data.copy() 
        data["movie_cover"] = request.FILES.get("movie_cover")
        data["user"] = request.user.id
        serializer = CreateMovieSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        response = serializer.save()
           
        return Response(MovieSerializer(response, context={'request': request}).data, HTTP_201_CREATED)

class GenreViewSet(GenericViewSet, ListModelMixin):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated]
