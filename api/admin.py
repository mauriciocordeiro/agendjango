from django.contrib import admin

from .models import Pessoa
from .models import Endereco
from .models import Telefone

# Register your models here.

admin.site.register(Pessoa)
admin.site.register(Endereco)
admin.site.register(Telefone)