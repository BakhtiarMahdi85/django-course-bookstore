from django.test import TestCase
from django.shortcuts import reverse

class HomePageTest(TestCase):

    def test_homepage_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    def test_homepage_url(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
    def test_hompage_contain(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'home page')
    def test_template_use(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')


