import factory

from django.contrib.auth import get_user_model
from django.utils import timezone

from ..models import Record, Project

User = get_user_model()


class ProjectFactory(factory.DjangoModelFactory):
    class Meta:
        model = Project
    
    name = 'name'
    description = 'descr'
    

class RecordFactory(factory.DjangoModelFactory):
    class Meta:
        model = Record
        
    time_spent = 5
    date = timezone.now().date()
    