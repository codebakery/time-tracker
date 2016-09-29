from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

User = get_user_model()


class TestUserCRUD(APITestCase):
    def setUp(self):
        self.password = '1234'
        self.user_data = {'username': 'test',
                          'password': self.password}
    
    def test_create_user(self):
        resp = self.client.post(reverse('users'), data=self.user_data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED, msg=str(resp.content))
        self.assertEqual(User.objects.filter(username=self.user_data['username']).count(), 1)
        
    def test_cant_create_user_without_password(self):
        data_no_pass = self.user_data.copy()
        del data_no_pass['password']
        resp = self.client.post(reverse('users'), data=data_no_pass)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST, msg=str(resp.content))
        
    def test_user_has_authtoken(self):
        resp = self.client.post(reverse('users'), data=self.user_data)
        try:
            Token.objects.get(user__username=self.user_data['username'])
        except Token.DoesNotExist:
            self.fail('user doesnt have auth token')