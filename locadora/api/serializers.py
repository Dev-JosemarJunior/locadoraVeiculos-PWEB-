from rest_framework import serializers

from .models import Endereco, Bairro, Cidade, Estado


class EnderecoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Endereco
        fields = ('logradouro', 'cep', 'complemento', 'bairro_id')
