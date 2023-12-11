from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class UserAppViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()

    def test_registration_view(self):
        response = self.client.get(reverse('user_app:registration'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get(reverse('user_app:login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('user_app:logout'))
        self.assertEqual(response.status_code, 302)

    def test_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('user_app:profile'))
        self.assertEqual(response.status_code, 200)
