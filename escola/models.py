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


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    validade = models.DateField()

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome
