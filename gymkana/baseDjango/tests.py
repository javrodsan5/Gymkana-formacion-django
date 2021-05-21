from django.test import TestCase
from .models import New
from django.urls import reverse
import unittest
from django.test import Client


class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        url = reverse('baseDjango:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['three_latest_news']), 3)
        self.assertEqual(len(response.context['three_latest_events']), 3)