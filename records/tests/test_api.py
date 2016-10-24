from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from registration.tests.factories import UserFactory
from .factories import ProjectFactory, RecordFactory
from ..models import Record, Project

User = get_user_model()


class TestRecordCRUD(APITestCase):
    def setUp(self):
        self.data = {
            'time_spent': 1.1,
            'date': timezone.now().date(),
        }
        self.user = UserFactory()
        # auth
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_create_record_without_project(self):
        resp = self.client.post(reverse('records'), self.data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED, msg=str(resp.content))
        self.assertEqual(Record.objects.count(), 1)

    def test_create_record_with_project_when_project_exist(self):
        project = ProjectFactory()
        self.data.update({'project': project.name})
        resp = self.client.post(reverse('records'), self.data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED, msg=str(resp.content))
        r = Record.objects.get(date=self.data['date'])
        self.assertEqual(r.project, project)


class TestRecordsVisibility(APITestCase):
    def setUp(self):
        self.user_A = UserFactory()
        self.user_B = UserFactory()
        self.record_A = RecordFactory(user=self.user_A, description='A_descr')
        self.record_B = RecordFactory(user=self.user_B, description='B_descr')

    def test_user_a_doesnt_see_records_from_user_b(self):
        # auth
        token = Token.objects.get(user__username=self.user_A.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        resp = self.client.get(reverse('records'))
        self.assertEqual(resp.status_code, status.HTTP_200_OK, msg=str(resp.content))
        self.assertIn(self.record_A.description, str(resp.content))
        self.assertNotIn(self.record_B.description, str(resp.content))


class TestRecordsDetailPermissions(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user_record = RecordFactory(user=self.user)
        self.user2 = UserFactory()
        self.user2_record = RecordFactory(user=self.user2)
        # auth
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_user_who_made_a_record_can_see_details(self):
        resp = self.client.get(reverse('record_detail', kwargs={'pk':self.user_record.pk}))
        self.assertEqual(resp.status_code, status.HTTP_200_OK, msg=str(resp.content))

    def test_user_cant_see_details_of_other_users_records(self):
        resp = self.client.get(reverse('record_detail', kwargs={'pk':self.user2_record.pk}))
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN, msg=str(resp.content))
