from django.db import models

# Create your models here.
class Menor(models.Model):
    nome_responsavel = models.CharField( max_length=50,verbose_name='Nome do Responsavel')
    idade_resp = models.IntegerField(verbose_name='Idade do responsavel')
    cpf_resp = models.IntegerField(verbose_name='CPF do responsavel')
    contato = models.IntegerField(verbose_name='Contato do responsavel')
    email = models.CharField(max_length=50, verbose_name='Email')
    senha = models.CharField(max_length=50, verbose_name='Senha')
    nome_menor = models.CharField(max_length=50, verbose_name='Nome do menor')
    idade_menor = models.IntegerField(verbose_name='Idade do menor')
    cpf_menor = models.IntegerField(verbose_name='CPF do menor')
    cep = models.IntegerField(verbose_name='CEP')
