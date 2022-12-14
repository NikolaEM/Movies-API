"""Movie_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from Movie_API import settings
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.urls import usersRouter, urlpatterns
from movie.urls import moviesRouter, genresRouter, commentsNestedRouter

router = DefaultRouter()
router.registry.extend(usersRouter.registry)
router.registry.extend(moviesRouter.registry)
router.registry.extend(genresRouter.registry)
router.registry.extend(commentsNestedRouter.registry)

urlpatterns = [
    path('', include(urlpatterns)),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(commentsNestedRouter.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
