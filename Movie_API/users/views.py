from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import UserSerializer, CreateUserSerializer, BlackListTokenSerializer


class UserViewSet(RetrieveModelMixin, GenericViewSet, CreateModelMixin):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        serializer = CreateUserSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        response = serializer.save()
           
        return Response(UserSerializer(response, context={'request': request}).data, HTTP_201_CREATED)

class BlacklistRefreshView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = BlackListTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(HTTP_204_NO_CONTENT)
        