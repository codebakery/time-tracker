from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Record, Project


User = get_user_model()


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description',)


class RecordSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Record
        fields = ('id', 'date', 'user', 'time_spent', 'issue', 'project', 'description',)
        read_only_fields = ('user',)

    def save(self, **kwargs):
        instance = super().save(user=self.context['request'].user)
        return instance


class RecordCSVSerializer(RecordSerializer):
    project = serializers.SlugRelatedField(slug_field='name', queryset=Project.objects.all(),
                                           allow_null=True, required=False)
    class Meta:
        model = Record
        fields = ('id', 'date', 'user', 'time_spent', 'issue', 'project', 'description',)
        read_only_fields = ('user',)
