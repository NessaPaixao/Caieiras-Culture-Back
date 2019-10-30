from rest_framework import serializers
from maior_dezoito.models import Responsavel


class ResponsavelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsavel
        fields = ('id','nome_completo','idade', 'genero','cpf', 'contato','cep','email','senha')
