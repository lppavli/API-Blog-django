from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import *


class PostTestCases(TestCase):

    def setUp(self) -> None:
        self.user1 = User.objects.create(username='testuser1', password='password')
        self.user2 = User.objects.create(username='testuser2', password='password')
        self.post = Post.objects.create(title='testtitle', description='testdescription')
        response = self.client.post('/api/v1/login/', {"username": 'testuser1', "password": 'password'})
        self.token = response.json()['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

