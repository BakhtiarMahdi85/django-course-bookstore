from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

class SigupTest(TestCase):
    username = 'myusername'
    email = 'myusername@gmail.com'

    def test_signup_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
    def test_signup_url(self):
        response = self.client.get('/accounts/')
        self.assertEqual(response.status_code, 200)
    def test_sigup_form(self):
        user = get_user_model().objects.create_user(
            self.username,
            self.email,
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)

