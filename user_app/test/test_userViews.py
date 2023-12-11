from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class UserAppViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()

    def test_registration_view_get_success(self):
        response = self.client.get(reverse('user_app:registration'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/signupMub.html')

    def test_registration_view_post_success(self):
        data = {
            'username': 'newuser',
            'password1': 'newpassword',
            'password2': 'newpassword',
        }
        response = self.client.post(reverse('user_app:registration'), data)
        self.assertEqual(response.status_code, 200) 


    def test_registration_view_form_errors(self):
        data = {
            'username': '',  # Invalid: Username is required
            'password1': 'password',
            'password2': 'password',
        }
        response = self.client.post(reverse('user_app:registration'), data)
        self.assertEqual(response.status_code, 200)  # Form validation error, so it should stay on the same page
        self.assertTemplateUsed(response, 'user/signupMub.html')
        self.assertContains(response, 'This field is required.')  # Adjust this based on your actual form error message

    def test_profile_view_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('user_app:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'share/profilePageMub.html')

    def test_profile_view_unauthenticated(self):
        response = self.client.get(reverse('user_app:profile'))
        self.assertEqual(response.status_code, 302)  # Redirects unauthenticated users
        self.assertRedirects(response, f"{reverse('user_app:login')}?next={reverse('user_app:profile')}")
