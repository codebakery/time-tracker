from django.contrib.auth import get_user_model
from django.utils.translation import ugettext as _

from rest_framework import status, generics


from .serializers import UserSerializer

User = get_user_model()


class Users(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer