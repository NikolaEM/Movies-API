from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import CustomUser
from .serializers import UserSerializer, CreateUserSerializer

class UserViewSet(RetrieveModelMixin, GenericViewSet, CreateModelMixin):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        serializer = CreateUserSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        response = serializer.save()
           
        return Response(UserSerializer(response, context={'request': request}).data, HTTP_201_CREATED)
        


