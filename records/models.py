from django.conf import settings
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    # owner = company/user ?
    
    
class Record(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    project = models.ForeignKey(Project, null=True, blank=True)
    time_spent = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
