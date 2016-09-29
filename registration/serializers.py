from django.contrib.auth import get_user_model

from rest_framework import serializers, exceptions
from rest_framework.reverse import reverse

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True,}}