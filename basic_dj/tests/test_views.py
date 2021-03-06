import tempfile
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class PublisherViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def _login(self):
        User.objects.create_user(username='foo', password='bar')
        self.client.login(username='foo', password='bar')

    def test_create_publisher(self):
        self._login()
        response = self.client.post(reverse('create_publisher'),
                                    {'name': 'test',
                                     'address': '4/333 Telengana Hyderabad',
                                     'city': 'Hyderabad',
                                     'state_province': 'Telengana',
                                     'country': 'INDIA',
                                     'website': 'https://www.google.com'})
        self.assertEqual(response.status_code, 200)

    def test_create_publisher_with_publisher_file_upload(self):
        self._login()
        testfile = tempfile.TemporaryFile()
        testfile.write('Some data happy life')
        testfile.seek(0)
        response = self.client.post(reverse('create_publisher'),
                                    {'name': 'test',
                                     'address': '4/333 Telengana Hyderabad',
                                     'city': 'Telengana',
                                     'state_province': 'Hyderabad',
                                     'country': 'INDIA',
                                     'website': 'https://www.google.com',
                                     'publisher_file': testfile})
        self.assertEqual(response.status_code, 302)

    # def test_detail_publisher(self):
