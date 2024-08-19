from django.test import TestCase
from django.urls import reverse

class IntegrationTestCase(TestCase):
    def test_interaccion(self):
        response = self.client.get(reverse('nombre_de_la_vista'))
        self.assertEqual(response.status_code, 200)