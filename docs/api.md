# API - agendjango

API para agenda de contatos.

Acesse no [Heroku](https://agendjango.herokuapp.com/).

## Recursos

### Pessoas

**GET** `/api/pessoas` - _Lista as pessoas da agenda_

```json
[
    {
        "nome": "",
        "sobrenome": "",
        "nascimento": null,
        "email": "",
        "telefones": [],
        "enderecos": []
    }
]
```

**GET** `/api/pessoas/:id` - _Retorna a pessoa, dado seu id_

```json
{
    "nome": "",
    "sobrenome": "",
    "nascimento": null,
    "email": "",
    "telefones": [],
    "enderecos": []
}
```


**POST** `/api/pessoas` - _Registra uma pessoa na agenda_

```json
{
    "nome": "",
    "sobrenome": "",
    "nascimento": "yyyy-mm-dd",
    "email": ""
}
```


## Entidades

### Pessoa

```json
{
    "nome": "",
    "sobrenome": "",
    "nascimento": null,
    "email": "",
    "telefones": [],
    "enderecos": []
}
```

### Telefone

```json
{
    "id_pessoa": null,
    "numero": "",
    "tipo": null
}
```
| tipo | descrição   |
|------|-------------|
| 1    | celular     |
| 2    | comercial   |
| 3    | fax         |
| 4    | residencial |


### Endereço

```json
{
    "id_pessoa": null,
    "logradouro": "",
    "numero": "",
    "complemento": "",
    "bairro": "",
    "cep": "",
    "cidade": "",
    "uf": "",
    "tipo": null
}
```
| tipo | descrição   |
|------|-------------|
| 1    | comercial   |
| 2    | residencial |