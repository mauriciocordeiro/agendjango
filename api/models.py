from django.db import models

# Create your models here.

class Pessoa(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, null=False)
    nome = models.CharField(max_length=32, blank=False, null=False)
    sobrenome = models.CharField(max_length=32, blank=False, null=False)
    nascimento = models.DateField()
    email = models.CharField(max_length=64)
    foto = models.BinaryField()

class Endereco(models.Model):
    TIPOS_CHOICES = [
        (1, 'Comercial'),
        (2, 'Residencial')
    ]

    id = models.IntegerField(primary_key=True, unique=True, null=False)
    id_pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE)
    logradouro = models.CharField(max_length=128, blank=False, null=False)
    numero = models.CharField(max_length=8)
    complemento = models.CharField(max_length=64, blank=True, null=True)
    bairro = models.CharField(max_length=32)
    cep = models.CharField(max_length=9, blank=True, null=True)
    cidade = models.CharField(max_length=32, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    tipo = models.IntegerField(choices=TIPOS_CHOICES)

    class Meta:
        unique_together = ('id', 'id_pessoa')

class Telefone(models.Model):
    TIPOS_CHOICES = [
        (1, 'Celular'),
        (2,'Comercial'),
        (3, 'Fax'),
        (4, 'Residencial')
    ]

    id = models.IntegerField(primary_key=True, unique=True, null=False)
    id_pessoa = models.ForeignKey('Pessoa', on_delete=models.CASCADE)
    numero = models.CharField(max_length=32, blank=False, null=False)
    tipo = models.IntegerField(choices=TIPOS_CHOICES)
    
    class Meta:
        unique_together = ('id', 'id_pessoa')
