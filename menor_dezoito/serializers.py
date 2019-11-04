from rest_framework import serializers
from menor_dezoito.models import Menor


class MenorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menor
        fields = ['id',
                  'nome_responsavel',
                  'idade_resp',
                  'cpf_resp',
                  'contato',
                  'email',
                  'senha'
                  'nome_menor',
                  'idade_menor',
                  'cpf_menor',
                  'cep',
                  ]