from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=150)
    cidade = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    curso = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
