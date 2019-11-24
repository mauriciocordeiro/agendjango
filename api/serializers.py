from rest_framework import serializers
from .models import Pessoa
from .models import Endereco
from .models import Telefone

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('id', 'nome', 'sobrenome', 'nascimento', 'email', 'foto')
        
class EnderecoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'id_pessoa', 'logradouro', 'numero', 'complemento', 'bairro', 'cep', 'cidade', 'uf', 'tipo')
        
class TelefoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Telefone
        fields = ('id', 'id_pessoa', 'numero', 'tipo')