from datetime import datetime
from django.test import TestCase
from news.models import New
from events.models import Event
from django.urls import reverse
from django.utils import timezone
import unittest
from django.test import Client


class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        New.objects.create(title="Titulo1", subtitle="subtitle1")
        New.objects.create(title="Titulo2", subtitle="subtitle2")
        New.objects.create(title="Titulo3", subtitle="subtitle3")
        New.objects.create(title="Titulo4", subtitle="subtitle4")

        Event.objects.create(title="Titulo1", subtitle="subtitle1", start_date= datetime(2021,5,21,tzinfo=timezone.utc), end_date= datetime(2021,6,21,tzinfo=timezone.utc))
        Event.objects.create(title="Titulo2", subtitle="subtitl2", start_date= datetime(2021,5,21,tzinfo=timezone.utc), end_date= datetime(2021,6,21,tzinfo=timezone.utc))
        Event.objects.create(title="Titulo3", subtitle="subtitle3", start_date= datetime(2021,5,21,tzinfo=timezone.utc), end_date= datetime(2021,6,21,tzinfo=timezone.utc))
        Event.objects.create(title="Titulo4", subtitle="subtitle4", start_date= datetime(2021,5,21,tzinfo=timezone.utc), end_date= datetime(2021,6,21,tzinfo=timezone.utc))


    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['three_latest_news']), 3)
        self.assertEqual(len(response.context['three_latest_events']), 3)