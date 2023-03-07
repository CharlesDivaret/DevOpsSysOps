from django.test import TestCase
from django.urls import reverse

class AuthorListViewTest(TestCase):
    @classmethod
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/jouer')
        self.assertEqual(response.status_code, 200)