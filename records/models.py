from django.conf import settings
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    # owner = company/user ?

    def __str__(self):
        return self.name


class Record(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    project = models.ForeignKey(Project, null=True, blank=True)
    time_spent = models.DecimalField(max_digits=5, decimal_places=2)
    issue = models.IntegerField(null=True, blank=True)  # github issue
    date = models.DateField()
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
