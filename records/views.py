from django.contrib.auth import get_user_model
from django.conf import settings
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from rest_framework import status, generics, settings as drf_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework_csv import renderers

from .models import Record, Project
from .serializers import RecordSerializer, ProjectSerializer

User = get_user_model()


class RecordsRenderer (renderers.CSVRenderer):
    header = ('date', 'user', 'time_spent', 'project', 'description', 'timestamp',)


api_settings = drf_settings.APISettings(None, drf_settings.DEFAULTS, drf_settings.IMPORT_STRINGS)

class Records(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = (IsAuthenticated,)
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES + [RecordsRenderer,]
    

class Projects(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)
