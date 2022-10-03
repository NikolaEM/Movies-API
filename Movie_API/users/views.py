from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_200_OK
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import CustomUser
from .serializers import UserSerializer, CreateUserSerializer, BlackListTokenSerializer

class UserViewSet(RetrieveModelMixin, GenericViewSet, CreateModelMixin):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = CreateUserSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        response = serializer.save()
           
        return Response(UserSerializer(response, context={'request': request}).data, HTTP_201_CREATED)

    @action(detail=False, url_path='me', permission_classes=[IsAuthenticated]) 
    def get_current_user(self, request):          
        response_serializer = UserSerializer(request.user)
        return Response(response_serializer.data, HTTP_200_OK)

class BlacklistRefreshView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = BlackListTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(HTTP_204_NO_CONTENT)
        