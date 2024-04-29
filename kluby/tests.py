from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from .views import wszystkie, szczegoly, nowy, usun, edytuj
from .models import Klub, ExtraInfo
class KlubyTests(TestCase):
    def setUp(self):
        User.objects.create_superuser(username='admin', password='admin')

    def test_urls_wszystkie(self):
        url = reverse('wszystkie')
        self.assertEquals(resolve(url).func, wszystkie)


    def test_urls_szczegoly(self):
        url = reverse('szczegoly', args=[10])
        self.assertEquals(resolve(url).func, szczegoly)

    def test_urls_nowy(self):
        url = reverse('nowy')
        self.assertEquals(resolve(url).func, nowy)


    def test_urls_edytuj_film(self):
        url = reverse('edytuj', args=[10])
        self.assertEquals(resolve(url).func, edytuj)

    def test_urls_usun(self):
        url = reverse('usun', args=[10])
        self.assertEquals(resolve(url).func, usun)


    def test_views_wszystkie(self):
        client = Client()
        response = client.get(reverse('wszystkie'))
        self.assertEquals(response.status_code,200)

    def test_views_wszystkie_templates(self):
        client = Client()
        response = client.get(reverse('wszystkie'))
        self.assertTemplateUsed(response, 'kluby/wszystkie.html')

    def test_views_szczegoly(self):
        Klub.objects.create(nazwa="Testowy klub")
        client = Client()
        response = client.get(reverse('szczegoly', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_views_szczegoly_templates(self):
        Klub.objects.create(nazwa="Testowy klub")
        client = Client()
        response = client.get(reverse('szczegoly', args=[1]))
        self.assertTemplateUsed(response, 'kluby/szczegoly.html')


    def test_views_edytuj(self):
        klub = Klub.objects.create(nazwa="Testowy klub")
        client = Client()
        client.login(username="admin", password="admin")
        response = client.get(reverse('edytuj', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_views_edytuj_templates(self):
        klub = Klub.objects.create(nazwa="Testowy klub")
        client = Client()
        client.login(username="admin", password="admin")
        response = client.get(reverse('edytuj', args=[1]))
        self.assertTemplateUsed(response, 'kluby/nowy.html')














