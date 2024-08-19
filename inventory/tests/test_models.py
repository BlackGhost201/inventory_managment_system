from django.test import TestCase
from inventory.models import Articulo, Comentario
from django.contrib.auth.models import User

class ArticuloModelTest(TestCase):

    def test_publicar(self):
        articulo = Articulo()
        self.assertIsNone(articulo.publicar())  # Asegura que el método publicar no retorna nada

    def test_editar(self):
        articulo = Articulo()
        self.assertIsNone(articulo.editar())  # Asegura que el método editar no retorna nada

class ComentarioModelTest(TestCase):

    def test_agregar_comentario(self):
        user = User.objects.create_user(username='testuser', password='12345')
        articulo = Articulo.objects.create()
        comentario = Comentario(autor=user, texto="Texto de prueba", articulo=articulo)
        self.assertIsNone(comentario.agregar_comentario())  # Asegura que el método agregar_comentario no retorna nada

    def test_editar_comentario(self):
        comentario = Comentario()
        self.assertIsNone(comentario.editar_comentario())  # Asegura que el método editar_comentario no retorna nada
