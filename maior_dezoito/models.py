from django.db import models


class Responsavel(models.Model):

    nome_completo = models.CharField( max_length=50, verbose_name='Nome Completo')
    idade = models.IntegerField(verbose_name='Idade')
    cpf = models.IntegerField(verbose_name='CPF')
    cep = models.IntegerField(verbose_name='CEP')
    contato = models.IntegerField(verbose_name='Contato')
    email = models.CharField(max_length=50, verbose_name='Email')
    senha = models.CharField(max_length=50, verbose_name='Senha')

