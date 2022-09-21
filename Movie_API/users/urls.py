from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView
from .views import  UserViewSet
from rest_framework.routers import SimpleRouter

usersRouter = SimpleRouter()
usersRouter.register(r'users', UserViewSet)

urlpatterns = [
   
]