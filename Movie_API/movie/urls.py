from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from .views import CommentView, GenreViewSet, MovieViewSet

moviesRouter = SimpleRouter()
moviesRouter.register(r'movies', MovieViewSet)

genresRouter = SimpleRouter()
genresRouter.register(r'genres', GenreViewSet)

commentsNestedRouter = NestedSimpleRouter(moviesRouter, r'movies')
commentsNestedRouter.register(r'comments', CommentView, basename='comments')