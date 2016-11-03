from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in

from rest_framework import status, generics
from rest_framework.authtoken import views as authtoken_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .serializers import UserSerializer, UserDetailSerializer
from .permissions import IsSameUser

User = get_user_model()


class Users(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (IsSameUser,)


class ObtainAuthToken(authtoken_view.ObtainAuthToken):
    """
    Get token for registered user.
    """
    def post(self, request):
        response = super().post(request)
        user = Token.objects.get(key=response.data['token']).user
        user_logged_in.send(sender=user.__class__, request=request, user=user)
        response.data.update({'url': reverse('user_detail', kwargs={'pk': user.pk}, request=request),
                              'id': user.id,
                              'token': user.auth_token.key})
        return Response(status=status.HTTP_200_OK, data=response.data)
