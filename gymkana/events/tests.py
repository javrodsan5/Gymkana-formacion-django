from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from .models import Event
from django.urls import reverse
from django.test import Client
from datetime import datetime


class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()
        Event.objects.create(title="Titulo", subtitle="subtitle",
                             start_date=datetime.now(), end_date=datetime.now())
        Event.objects.create(title="BorrarV2", subtitle="subtitle",
                             start_date=datetime.now(), end_date=datetime.now())

    def test_V2_create_event_complete(self):
        data = {"title": "Super Test", "subtitle": "Subtitulo",
                "body": "Cuerpo", "start_date": "2021-05-29", "end_date": "2022-05-29"}
        response = self.client.get('/events/v2/events/create')
        self.assertTemplateUsed(response, "events/create_eventV2.html")

        old_size = Event.objects.all().count()
        response = self.client.post('/events/v2/events/create', data=data)
        new_size = Event.objects.all().count()
        self.assertIs(old_size < new_size, True)
        self.assertEqual(Event.objects.last().title, "Super Test")

    def test_V2_create_event_negative_end_after_start(self):
        data = {"title": "Test bad date", "subtitle": "Subtitulo",
                "body": "Cuerpo", "start_date": "2022-05-29", "end_date": "2021-05-29"}
        response = self.client.get('/events/v2/events/create')
        self.assertTemplateUsed(response, "events/create_eventV2.html")

        old_size = Event.objects.all().count()
        response = self.client.post('/events/v2/events/create', data=data)
        new_size = Event.objects.all().count()
        self.assertIs(old_size == new_size, True)
        self.assertIsNot(Event.objects.last().title, "Test bad date")

    def test_V2_create_event_negative_title(self):
        data = {"title": "Test titulo demasiado largo", "subtitle": "Subtitulo",
                "body": "Cuerpo", "start_date": "2022-05-29", "end_date": "2021-05-29"}
        response = self.client.get('/events/v2/events/create')
        self.assertTemplateUsed(response, "events/create_eventV2.html")

        old_size = Event.objects.all().count()
        response = self.client.post('/events/v2/events/create', data=data)
        new_size = Event.objects.all().count()
        self.assertIs(old_size == new_size, True)
        self.assertIsNot(Event.objects.last().title,
                         "Test titulo demasiado largo")

    def test_V2_create_event_negative_subtitle(self):
        data = {"title": "Test titulo", "subtitle": "Test subtitulo demasiado largo",
                "body": "Cuerpo", "start_date": "2022-05-29", "end_date": "2021-05-29"}
        response = self.client.get('/events/v2/events/create')
        self.assertTemplateUsed(response, "events/create_eventV2.html")

        old_size = Event.objects.all().count()
        response = self.client.post('/events/v2/events/create', data=data)
        new_size = Event.objects.all().count()
        self.assertIs(old_size == new_size, True)
        self.assertIsNot(Event.objects.last().subtitle,
                         "Test subtitulo demasiado largo")

    def test_V2_update_event_complete(self):
        data = {"title": "Super Test", "subtitle": "Subtitulo",
                "body": "Cuerpo", "start_date": "2021-05-29", "end_date": "2022-05-29"}
        response = self.client.get('/events/v2/events/1/update')
        self.assertTemplateUsed(response, "events/updateV2.html")

        old_size = Event.objects.all().count()
        response = self.client.post('/events/v2/events/1/update', data=data)
        new_size = Event.objects.all().count()
        self.assertIs(old_size == new_size, True)
        self.assertEqual(Event.objects.get(id=1).title, "Super Test")

    def test_V2_detail_event(self):
        new = Event.objects.get(id=1)
        response = self.client.get(
            reverse('events:event_detailsV2', args=(new.id,)))
        self.assertEqual(response.status_code, 200)

    def test_V2_list_all_events(self):
        url = reverse('events:list_all_eventsV2')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['events']), 2)

    def test_delete_eventV2(self):
        old_size = Event.objects.all().count()

        post_response = self.client.post(
            reverse('events:event_deleteV2', args=(2,)), follow=True)
        self.assertRedirects(post_response, reverse(
            'events:list_all_eventsV2'), status_code=302)

        new_size = Event.objects.all().count()
        self.assertIs(old_size > new_size, True)
