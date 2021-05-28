from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from .models import New
from django.urls import reverse
from django.test import Client
from django.conf import settings
import tempfile


class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()
        settings.MEDIA_ROOT = tempfile.mkdtemp()
        New.objects.create(title="Titulo", subtitle="subtitle")
        New.objects.create(title="BorrarV1", subtitle="subtitle")
        New.objects.create(title="BorrarV2", subtitle="subtitle")

    def test_V1_list_all_news(self):
        url = reverse('news:list_all_newsV1')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['news']), 3)

    def test_V1_detail(self):
        new = New.objects.get(id=1)
        response = self.client.get(reverse('news:detailsV1', args=(new.id,)))
        self.assertEqual(response.status_code, 200)

    def test_V1_delete_new(self):
        old_size = New.objects.all().count()
        new = New.objects.get(id=2)
        response = self.client.get(reverse('news:deletenewV1', args=(new.id,)))
        new_size = New.objects.all().count()
        self.assertEqual(response.status_code, 302)
        self.assertIs(old_size > new_size, True)

    def test_V1_create_new_complete(self):
        data = {"title": "Super Test", "subtitle": "Subtitulo",
                "body": "Cuerpo", "image": "/static/news/images/new.png"}
        response = self.client.get('/news/v1/news/create')
        self.assertTemplateUsed(response, "news/createV1.html")

        old_size = New.objects.all().count()
        response = self.client.post('/news/v1/news/create', data=data)
        new_size = New.objects.all().count()
        self.assertIs(old_size < new_size, True)
        self.assertEqual(New.objects.last().title, "Super Test")

    def test_V1_create_new_with_image(self):
        imagen = SimpleUploadedFile(name='foto.jpg', content=open(
            './testSampleImages/foto.jpg', 'rb').read(), content_type='image/jpg')
        data = {"title": "Super Test", "subtitle": "Subtitulo",
                "body": "Cuerpo", "image": imagen}
        response = self.client.get('/news/v1/news/create')
        self.assertTemplateUsed(response, "news/createV1.html")

        old_size = New.objects.all().count()
        response = self.client.post('/news/v1/news/create', data=data)
        new_size = New.objects.all().count()
        self.assertIs(old_size < new_size, True)
        self.assertEqual(New.objects.last().title, "Super Test")

    def test_V1_create_new_with_bad_image(self):
        imagen = SimpleUploadedFile(name='8MB.jpg', content=open(
            './testSampleImages/8MB.jpeg', 'rb').read(), content_type='image/jpeg')
        data = {"title": "Super Test", "subtitle": "Subtitulo",
                "body": "Cuerpo", "image": imagen}
        response = self.client.get('/news/v1/news/create')
        self.assertTemplateUsed(response, "news/createV1.html")

        old_size = New.objects.all().count()
        response = self.client.post('/news/v1/news/create', data=data)
        new_size = New.objects.all().count()
        self.assertIs(old_size == new_size, True)
        self.assertIsNot(New.objects.last().title, "Super Test")

    def test_V1_create_new_with_bad_image_pdf_as_png(self):
        imagen = SimpleUploadedFile(name='Trabajando con Git.png', content=open(
            './testSampleImages/Trabajando con Git.png', 'rb').read(), content_type='image/png')
        data = {"title": "Super Test", "subtitle": "Subtitulo",
                "body": "Cuerpo", "image": imagen}
        response = self.client.get('/news/v1/news/create')
        self.assertTemplateUsed(response, "news/createV1.html")

        old_size = New.objects.all().count()
        response = self.client.post('/news/v1/news/create', data=data)
        new_size = New.objects.all().count()
        self.assertIs(old_size == new_size, True)
        self.assertIsNot(New.objects.last().title, "Super Test")

    def test_V1_create_new_noImage(self):
        data = {"title": "Test no image",
                "subtitle": "Subtitulo", "body": "Cuerpo"}
        response = self.client.get('/news/v1/news/create')
        self.assertTemplateUsed(response, "news/createV1.html")

        old_size = New.objects.all().count()
        response = self.client.post('/news/v1/news/create', data=data)
        new_size = New.objects.all().count()
        self.assertIs(old_size < new_size, True)
        self.assertEqual(New.objects.last().title, "Test no image")

    def test_V1_create_new_title_too_large(self):
        imagen = SimpleUploadedFile(name='foto.jpg', content=open(
            './testSampleImages/foto.jpg', 'rb').read(), content_type='image/jpg')
        data = {"title": "Test con titulo demasiado largo", "subtitle": "Subtitulo",
                "body": "Cuerpo", "image": imagen}
        response = self.client.get('/news/v1/news/create')
        self.assertTemplateUsed(response, "news/createV1.html")

        old_size = New.objects.all().count()
        response = self.client.post('/news/v1/news/create', data=data)
        new_size = New.objects.all().count()
        self.assertIs(old_size == new_size, True)
        self.assertIsNot(New.objects.last().title,
                         "Test con titulo demasiado largo")

    def test_V1_create_new_subtitle_too_large(self):
        imagen = SimpleUploadedFile(name='foto.jpg', content=open(
            './testSampleImages/foto.jpg', 'rb').read(), content_type='image/jpg')
        data = {"title": "Test", "subtitle": "Test con subtitulo demasiado largo",
                "body": "Cuerpo", "image": imagen}
        response = self.client.get('/news/v1/news/create')
        self.assertTemplateUsed(response, "news/createV1.html")

        old_size = New.objects.all().count()
        response = self.client.post('/news/v1/news/create', data=data)
        new_size = New.objects.all().count()
        self.assertIs(old_size == new_size, True)
        self.assertIsNot(New.objects.last().subtitle,
                         "Test con subtitulo demasiado largo")

    def test_V1_update_new_complete(self):
        imagen = SimpleUploadedFile(name='foto.jpg', content=open(
            './testSampleImages/foto.jpg', 'rb').read(), content_type='image/jpg')
        data = {"title": "Actualizado", "subtitle": "Subtitulo",
                "body": "Cuerpo", "image": imagen}
        response = self.client.get('/news/v1/1/update')
        self.assertTemplateUsed(response, "news/updateV1.html")

        old_size = New.objects.all().count()
        response = self.client.post('/news/v1/1/update', data=data)
        new_size = New.objects.all().count()
        self.assertIs(old_size == new_size, True)
        self.assertEqual(New.objects.get(id=1).title, "Actualizado")

    def test_V1_update_new_no_image(self):
        data = {"title": "Actualizado", "subtitle": "Subtitulo",
                "body": "Cuerpo"}
        response = self.client.get('/news/v1/1/update')
        self.assertTemplateUsed(response, "news/updateV1.html")

        old_size = New.objects.all().count()
        response = self.client.post('/news/v1/1/update', data=data)
        new_size = New.objects.all().count()
        self.assertIs(old_size == new_size, True)
        self.assertEqual(New.objects.get(id=1).title, "Actualizado")

    def test_V1_update_new_title_too_large(self):
        imagen = SimpleUploadedFile(name='foto.jpg', content=open(
            './testSampleImages/foto.jpg', 'rb').read(), content_type='image/jpg')
        data = {"title": "Actualizado pero demasiado largo", "subtitle": "Subtitulo",
                "body": "Cuerpo", "image": imagen}
        response = self.client.get('/news/v1/1/update')
        self.assertTemplateUsed(response, "news/updateV1.html")

        old_size = New.objects.all().count()
        response = self.client.post('/news/v1/1/update', data=data)
        new_size = New.objects.all().count()
        self.assertIs(old_size == new_size, True)
        self.assertIsNot(New.objects.get(id=1).title,
                         "Actualizado pero demasiado largo")

# ---------------------------------V2--------------------------

    def test_V2_create_new_complete(self):
        imagen = SimpleUploadedFile(name='foto.jpg', content=open(
            './testSampleImages/foto.jpg', 'rb').read(), content_type='image/jpg')
        data = {"title": "Super Test", "subtitle": "Subtitulo",
                "body": "Cuerpo", "image": imagen}
        response = self.client.get('/news/v2/news/create')
        self.assertTemplateUsed(response, "news/createV2.html")

        old_size = New.objects.all().count()
        response = self.client.post('/news/v2/news/create', data=data)
        new_size = New.objects.all().count()
        self.assertIs(old_size < new_size, True)
        self.assertEqual(New.objects.last().title, "Super Test")

    def test_V2_create_new_noImage(self):
        data = {"title": "Test no image",
                "subtitle": "Subtitulo", "body": "Cuerpo"}
        response = self.client.get('/news/v2/news/create')
        self.assertTemplateUsed(response, "news/createV2.html")

        old_size = New.objects.all().count()
        response = self.client.post('/news/v2/news/create', data=data)
        new_size = New.objects.all().count()
        self.assertIs(old_size < new_size, True)
        self.assertEqual(New.objects.last().title, "Test no image")

    def test_V2_create_new_title_too_large(self):
        imagen = SimpleUploadedFile(name='foto.jpg', content=open(
            './testSampleImages/foto.jpg', 'rb').read(), content_type='image/jpg')

        data = {"title": "Test con titulo demasiado largo", "subtitle": "Subtitulo",
                "body": "Cuerpo", "image": imagen}
        response = self.client.get('/news/v2/news/create')
        self.assertTemplateUsed(response, "news/createV2.html")

        old_size = New.objects.all().count()
        response = self.client.post('/news/v2/news/create', data=data)
        new_size = New.objects.all().count()
        self.assertIs(old_size == new_size, True)
        self.assertIsNot(New.objects.last().title,
                         "Test con titulo demasiado largo")

    def test_V2_create_new_subtitle_too_large(self):
        imagen = SimpleUploadedFile(name='foto.jpg', content=open(
            './testSampleImages/foto.jpg', 'rb').read(), content_type='image/jpg')
        data = {"title": "Test", "subtitle": "Test con subtitulo demasiado largo",
                "body": "Cuerpo", "image": imagen}
        response = self.client.get('/news/v2/news/create')
        self.assertTemplateUsed(response, "news/createV2.html")

        old_size = New.objects.all().count()
        response = self.client.post('/news/v2/news/create', data=data)
        new_size = New.objects.all().count()
        self.assertIs(old_size == new_size, True)
        self.assertIsNot(New.objects.last().subtitle,
                         "Test con subtitulo demasiado largo")

    def test_delete_newV2(self):
        old_size = New.objects.all().count()

        response = self.client.get(
            reverse('news:deletenewV2', args=(3,)), follow=True)
        self.assertContains(response, 'Are you sure you want to delete')

        post_response = self.client.post(
            reverse('news:deletenewV2', args=(3,)), follow=True)
        self.assertRedirects(post_response, reverse(
            'news:list_all_newsV2'), status_code=302)

        new_size = New.objects.all().count()
        self.assertEqual(response.status_code, 200)
        self.assertIs(old_size > new_size, True)

    def test_V2_update_new_complete(self):
        data = {"title": "ActualizadoV2", "subtitle": "Subtitulo",
                "body": "Cuerpo", "image": "/static/news/images/new.png"}
        response = self.client.get('/news/v2/1/update')
        self.assertTemplateUsed(response, "news/updateV2.html")

        old_size = New.objects.all().count()
        response = self.client.post('/news/v2/1/update', data=data)
        new_size = New.objects.all().count()
        self.assertIs(old_size == new_size, True)
        self.assertEqual(New.objects.get(id=1).title, "ActualizadoV2")
