from rest_framework.routers import SimpleRouter
from .views import MovieViewSet

moviesRouter = SimpleRouter()
moviesRouter.register(r'movies', MovieViewSet)