from django.db import models


class Responsavel(models.Model):
    nome_completo = models.CharField( max_length=50,verbose_name='Nome Completo')
    idade = models.IntegerField(max_length=50, verbose_name='Idade')
    genero = models.CharField(max_length=50, verbose_name='Gênero')
    cpf = models.IntegerField(max_length=50, verbose_name='CPF')
    contato = models.IntegerField(max_length=50, verbose_name='Contato')
    cep = models.IntegerField(max_length=50, verbose_name='CEP')
    email = models.CharField(max_length=50, verbose_name='Email')
    senha = models.CharField(max_length=50, verbose_name='Senha')