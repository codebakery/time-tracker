from django.contrib.auth import get_user_model
from rest_framework import serializers, exceptions
from rest_framework.reverse import reverse

from .models import Record, Project


User = get_user_model()


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('user', 'project', 'time_spent', 'date', 'description', 'timestamp',)
        read_only_fields = ('user', 'timestamp')
        
        
    def save(self, **kwargs):
        instance = super().save(user=self.context['request'].user)
        return instance
        

class ProjectSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Project
        fields = ('name', 'description',)