from django.contrib import admin
from daterange_filter.filter import DateRangeFilter


from . import models


class ProjectAdmin(admin.ModelAdmin):
    model = models.Project
    list_display = ['name', 'description']
    list_display_links = ['name']

admin.site.register(models.Project, ProjectAdmin)


class RecordAdmin(admin.ModelAdmin):
    model = models.Record
    list_display = ['id', 'time_spent', 'date', 'user', 'description', 'timestamp']
    list_display_links = ['id', 'time_spent']
    list_filter = ['user', ('date', DateRangeFilter)]

admin.site.register(models.Record, RecordAdmin)
