from django.contrib.auth import get_user_model

from rest_framework import serializers, exceptions
from rest_framework.reverse import reverse

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        if validated_data.get('password'):
            user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            pwd = validated_data.pop('password')
            instance.set_password(pwd)
            instance.save()
        return super(UserSerializer, self).update(instance, validated_data)


class UserDetailSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name',)
        extra_kwargs = {'password': {'write_only': True}}