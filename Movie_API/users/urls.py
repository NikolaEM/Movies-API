from rest_framework.routers import SimpleRouter
from django.urls import path
from django.conf import settings
from django.contrib.auth import logout
from .views import  BlacklistRefreshView, UserViewSet

usersRouter = SimpleRouter()
usersRouter.register(r'users', UserViewSet)

urlpatterns = [
path('api/logout', BlacklistRefreshView.as_view(), name="logout"),
]