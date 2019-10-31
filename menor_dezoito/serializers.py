from rest_framework import serializers
from menor_dezoito.models import Menor


class MenorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menor
        fields = ('id',
                  'nome_responsavel',
                  'idade_resp',
                  'cpf',
                  'genero_resp',
                  'contato',
                  'cep',
                  'nome_menor',
                  'idade_menor',
                  'genero',
                  'email',
                  'senha'
                  )