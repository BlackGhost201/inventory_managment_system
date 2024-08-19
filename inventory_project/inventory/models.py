from django.db import models

# Create your models here.
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def registrar(self):
        pass

    def iniciar_sesion(self):
        pass

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def publicar(self):
        pass

    def editar(self):
        pass

class Comentario(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    texto = models.TextField()
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)

    def agregar_comentario(self):
        pass

    def editar_comentario(self):
        pass