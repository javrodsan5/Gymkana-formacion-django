from django.test import TestCase
from .models import New
from django.urls import reverse
from django.test import Client


class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()
        New.objects.create(title="Titulo", subtitle="subtitle")

    def test_list_all_newsV1(self):
        url = reverse('news:list_all_newsV1')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['news']), 1)

    def test_create_new(self):
        old_size = New.objects.all().count()
        url = self.client.get(reverse('news:create_newsV1'))
#terminar
        new_size = New.objects.all().count()
        self.assertIs(old_size == new_size, True)

    def test_detailV1(self):
        new = New.objects.get(id=1)
        response = self.client.get(reverse('news:detailsV1', args=(new.id,)))
        self.assertEqual(response.status_code, 200)
    
    def test_delete_newV1(self):
        old_size = New.objects.all().count()
        new = New.objects.create(title="Titulo", subtitle="subtitle")
        response = self.client.get(reverse('news:deletenewV1', args=(new.id,)))
        new_size = New.objects.all().count()
        self.assertEqual(response.status_code, 302)
        self.assertIs(old_size == new_size, True)

    def test_delete_newV2(self):
        old_size = New.objects.all().count()
        print(old_size)
        new = New.objects.create(title="Titulo", subtitle="subtitle")
        actual_size = New.objects.all().count()
        print(actual_size)
        response = self.client.get(reverse('news:deletenewV2', args=(new.id,)))
        new_size = New.objects.all().count()
        print( new_size)
        self.assertEqual(response.status_code, 200)
        self.assertIs(old_size == new_size, True)
