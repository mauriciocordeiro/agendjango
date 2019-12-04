from rest_framework import serializers
from .models import Pessoa
from .models import Endereco
from .models import Telefone

class PessoaSerializer(serializers.ModelSerializer):
    telefones = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    enderecos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Pessoa
        fields = ('id', 'nome', 'sobrenome', 'nascimento', 'email', 'foto', 'telefones', 'enderecos')
        
class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'id_pessoa', 'logradouro', 'numero', 'complemento', 'bairro', 'cep', 'cidade', 'uf', 'tipo')
        
class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = ('id', 'id_pessoa', 'numero', 'tipo')