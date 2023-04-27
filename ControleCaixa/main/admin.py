from django.contrib import admin
from main.models import *
# Register your models here.    
@admin.register(Cliente)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("nomeCliente",)

@admin.register(Caixa)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("codCaixa",)

@admin.register(CaixaCliente)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("idCliente","idCaixa")