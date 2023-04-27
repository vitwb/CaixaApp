from django.shortcuts import render
from main.models import *
# Create your views here.
def main(request):
    Clientes = Cliente.objects.all()
    Caixas = Caixa.objects.all()
    CaixaClientes = CaixaCliente.objects.all()
    return render(request,'index.html',{"Clientes":Clientes,"Caixas":Caixas,"CaixaClientes":CaixaClientes})