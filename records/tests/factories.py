import factory

from django.contrib.auth import get_user_model

from ..models import Record, Project

User = get_user_model()


class ProjectFactory(factory.DjangoModelFactory):
    class Meta:
        model = Project
    
    name = 'name'
    description = 'descr'
    