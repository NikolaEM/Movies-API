from rest_framework import serializers
from .models import CustomUser

regex_password= "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,50}$"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'name')

class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.RegexField(regex_password, required=True, allow_blank=False)

    def create(self, data):
        return CustomUser.objects.create_user(**data)

    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'password')
