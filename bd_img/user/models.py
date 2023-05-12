from django.db import models

class User(models.Model):
    nome = models.CharField(max_length=200)
    foto = models.ImageField(upload_to="imagens/")