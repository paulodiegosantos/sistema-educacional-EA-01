from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()

    cursos = models.ManyToManyField('Curso', blank=True)

class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()

