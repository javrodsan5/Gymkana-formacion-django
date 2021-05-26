from django.test import TestCase
from .models import New
from django.urls import reverse
from django.test import Client


class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()
        New.objects.create(title="Titulo", subtitle="subtitle")
        New.objects.create(title="BorrarV1", subtitle="subtitle")
        New.objects.create(title="BorrarV2", subtitle="subtitle")


    def test_V1_list_all_news(self):
        url = reverse('news:list_all_newsV1')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['news']), 1)

#     def test_V1_create_new(self):
#         old_size = New.objects.all().count()
#         url = self.client.get(reverse('news:create_newsV1'))
# #terminar
#         new_size = New.objects.all().count()
#         self.assertIs(old_size == new_size, True)
    
    def test_V2_create_new(self):
        self.client.post('/v2/news/create/', {'title': "Super Test", 'subtitle':"Subtitulo", 'body': "Cuerpo"})
        self.assertEqual(New.objects.last().title, "Super Test")

    def test_V1_detail(self):
        new = New.objects.get(id=1)
        response = self.client.get(reverse('news:detailsV1', args=(new.id,)))
        self.assertEqual(response.status_code, 200)
    
    def test_V1_delete_new(self):
        old_size = New.objects.all().count()
        new = New.objects.create(title="Titulo", subtitle="subtitle")
        response = self.client.get(reverse('news:deletenewV1', args=(new.id,)))
        new_size = New.objects.all().count()
        self.assertEqual(response.status_code, 302)
        self.assertIs(old_size == new_size, True)

    def test_delete_newV2(self):
        old_size = New.objects.all().count()
        print(old_size)
        
        response = self.client.get(reverse('news:deletenewV2', args=(3,)), follow=True)
        self.assertContains(response, 'Are you sure you want to remove')

        post_response = self.client.post(reverse('news:deletenewV2', args=(3,)), follow=True)
        self.assertRedirects(post_response, reverse('myclass_removed'), status_code=302)
        
        new_size = New.objects.all().count()
        print( new_size)
        self.assertEqual(response.status_code, 200)
        self.assertIs(old_size == new_size, True)
