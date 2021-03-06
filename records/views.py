from django.contrib.auth import get_user_model
from rest_framework import generics, settings as drf_settings, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework_csv import renderers
import django_filters

from .models import Record, Project
from .serializers import RecordSerializer, RecordCSVSerializer, ProjectSerializer
from records.permissions import IsOwner

User = get_user_model()


class RecordsRenderer (renderers.CSVRenderer):
    header = ('date', 'user', 'time_spent', 'project', 'description', 'issue')

    def render(self, data, *args, **kwargs):
        if not isinstance(data, list):
            data = data.get('results', [])
        return super(RecordsRenderer, self).render(data, *args, **kwargs)


api_settings = drf_settings.APISettings(None, drf_settings.DEFAULTS, drf_settings.IMPORT_STRINGS)


class RecordsFilter(filters.FilterSet):
    date = django_filters.DateFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}))

    class Meta:
        model = Record
        fields = ('date', 'user', 'project', )


class Records(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = (IsAuthenticated,)
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES + [RecordsRenderer]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = RecordsFilter

    def get_queryset(self):
        queryset = Record.objects.all()
        if self.request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if isinstance(self.perform_content_negotiation(self.request)[0], RecordsRenderer):
            return RecordCSVSerializer
        else:
            return self.serializer_class


class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = (IsAuthenticated, IsOwner)
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES + [RecordsRenderer]


class Projects(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)
