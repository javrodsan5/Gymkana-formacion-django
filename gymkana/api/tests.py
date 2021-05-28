from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from events.models import Event
from django.test import Client


class AccountTests(APITestCase):
    def setUp(self):
        self.client = Client()
        Event.objects.create(title="Titulo", subtitle="subtitle",
                             start_date="2021-05-06", end_date="2021-06-06")
        Event.objects.create(title="Segundo", subtitle="subtitle",
                             start_date="2021-05-06", end_date="2021-06-06")

    def test_2create_positive(self):
        url = reverse('api:listApi')
        data = {'title': 'Elecciones', 'subtitle': 'generales',
                'body': 'mueve el body', 'start_date': '2021-05-05', 'end_date': '2022-05-05'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.count(), 3)
        self.assertEqual(Event.objects.get(id=3).title, 'Elecciones')

    def test_3create_negative(self):
        url = reverse('api:listApi')
        data = {'title': 'Juanito', 'subtitle': 'generales',
                'body': 'mueve el body', 'start_date': '2022-05-05', 'end_date': '2021-05-05'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Event.objects.count(), 2)

    def test_1delete(self):
        url = reverse('api:detailsApi', args=(1,))
        old_size = Event.objects.all().count()
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        new_size = Event.objects.all().count()
        self.assertIs(old_size > new_size, True)

    # def test_update_positive(self):
    #     url = reverse('api:detailsApi', args=(2,))
    #     data = {'title': 'Cambio titulo', 'subtitle': 'generales',
    #             'body': 'mueve el body', 'start_date': '2021-05-05', 'end_date': '2022-05-05'}
    #     response = self.client.put(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(Event.objects.count(), 2)
    #     self.assertEqual(Event.objects.get(id=2).title, 'Cambio titulo')
