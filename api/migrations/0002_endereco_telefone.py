# Generated by Django 2.2.7 on 2019-11-24 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('numero', models.CharField(max_length=32)),
                ('tipo', models.IntegerField(choices=[(1, 'Celular'), (2, 'Comercial'), (3, 'Fax'), (4, 'Residencial')])),
                ('id_pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('logradouro', models.CharField(max_length=128)),
                ('numero', models.CharField(max_length=8)),
                ('complemento', models.CharField(max_length=64)),
                ('bairro', models.CharField(max_length=32)),
                ('cep', models.CharField(max_length=9)),
                ('cidade', models.CharField(max_length=32)),
                ('uf', models.CharField(max_length=2)),
                ('tipo', models.IntegerField(choices=[(1, 'Comercial'), (2, 'Residencial')])),
                ('id_pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Pessoa')),
            ],
            options={
                'unique_together': {('id', 'id_pessoa')},
            },
        ),
    ]
