from django.db import models
import uuid

class Genero(models.TextChoices):
    DRAMA = "DRAMA"
    ROMANCE = "ROMANCE"
    EPICO = "EPICO"
    AVENTURA = "AVENTURA"
    DISTOPIA = "DISTOPIA"
    CONTO = "CONTO"
    FANTASIA = "FANTASIA"
    SOBRENATURAL = "SOBRENATURAL"
    TERROR = "TERROR"
    DEFAULT = "NEUTRO"

class Book(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    number_pages = models.PositiveIntegerField()
    gender = models.CharField(max_length=50, choices=Genero.choices, default=Genero.DEFAULT)

class Following (models.Model):
    book = models.ForeignKey("livros.Book", on_delete=models.RESTRICT)
    user = models.ForeignKey("users.User", on_delete=models.RESTRICT)

