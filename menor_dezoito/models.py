from django.db import models

# Create your models here.
class Menor(models.Model):
    nome_responsavel = models.CharField( max_length=50,verbose_name='Nome do Responsavel')
    idade_resp = models.IntegerField(max_length=50, verbose_name='Idade do responsavel')
    genero_resp = models.CharField(max_length=50, verbose_name='Gênero do responsavel')
    cpf = models.IntegerField(max_length=50, verbose_name='CPF do responsavel')
    contato = models.IntegerField(max_length=50, verbose_name='Contato')
    cep = models.IntegerField(max_length=50, verbose_name='CEP')
    nome_menor = models.CharField(max_length=50, verbose_name='Nome do menor')
    idade_menor = models.IntegerField(max_length=50, verbose_name='Idade do menor')
    genero = models.CharField(max_length=50, verbose_name='Gênero do menor')
    email = models.CharField(max_length=50, verbose_name='Email')
    senha = models.CharField(max_length=50, verbose_name='Senha')