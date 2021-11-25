from django.contrib import admin
from .models import Endereco, Bairro, Cidade, Estado

admin.site.register(Endereco)
admin.site.register(Bairro)
admin.site.register(Cidade)
admin.site.register(Estado)
