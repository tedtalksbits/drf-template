from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}} # This will make the password field write only which means it will not be returned in the response

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
