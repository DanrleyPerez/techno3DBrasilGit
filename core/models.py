from django.db import models
# Create your models here.


class Conta(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=30)
    amount = models.DecimalField(decimal_places=3, max_digits=10)


class Lead(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=30)
    telefone = models.DecimalField(decimal_places=0,max_digits=11)
    email = models.EmailField()
    mensagem = models.CharField(max_length=200)


class entraremContato(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=50)
    motivo = models.CharField(max_length=50)
