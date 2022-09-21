from rest_framework.routers import SimpleRouter
from .views import  UserViewSet

usersRouter = SimpleRouter()
usersRouter.register(r'users', UserViewSet)