from rest_framework.routers import SimpleRouter
from .views import GenreViewSet, MovieViewSet

moviesRouter = SimpleRouter()
moviesRouter.register(r'movies', MovieViewSet)
genresRouter = SimpleRouter()
genresRouter.register(r'genres', GenreViewSet)