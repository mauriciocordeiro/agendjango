from django.shortcuts import render
from rest_framework import viewsets

from .models import Pessoa
from .models import Endereco
from .models import Telefone

from .serializers import PessoaSerializer
from .serializers import EnderecoSerializer
from .serializers import TelefoneSerializer

# Create your views here.

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all().order_by('nome')
    serializer_class = PessoaSerializer
    
class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all().order_by('logradouro')
    serializer_class = EnderecoSerializer
    
class TelefoneViewSet(viewsets.ModelViewSet):
    queryset = Telefone.objects.all().order_by('numero')
    serializer_class = TelefoneSerializer
