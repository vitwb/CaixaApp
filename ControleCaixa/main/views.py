from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from main.forms import FormsCaixa
from main.models import *
# Create your views here.

def main(request):
    Clientes = Cliente.objects.all()
    Caixas = Caixa.objects.all()
    CaixaClientes = CaixaCliente.objects.all()
    return render(request,'index.html',{"Clientes":Clientes,"Caixas":Caixas,"CaixaClientes":CaixaClientes})

def caixas(request):    
    if request.method =="GET":
        Caixas = Caixa.objects.all()
        form = FormsCaixa()
        context = {
            "Caixas":Caixas,
            "form":form
            }
        return render(request,'Caixas.html',context)
    
    elif request.method =="POST":
       
        codCaixa = request.POST.get('nomecaixa',None)
        caixa = Caixa(codCaixa=codCaixa)
        
        caixa.save()
        
       
        return HttpResponseRedirect('caixas')

def clientes(request):
    
    
    if request.method =="GET":
        Clientes = Cliente.objects.all()    
        
        return render(request,'Clientes.html',{"Clientes":Clientes})

    elif request.method =="POST":
        Clientes = request.POST.get('nomecliente',None)
        codCliente = request.POST.get('codcliente',None)
        
        Clienteobj = Cliente(nomeCliente=Clientes, codCliente = codCliente)
        Clienteobj.save()
        
        return HttpResponseRedirect('clientes')
    

def deleteCaixa(request, caixa_id):
    
    caixa = Caixa.objects.get(pk=caixa_id)
    caixa.delete()
    return redirect('caixas')


def deleteCliente(request, cliente_id):
    
    Cleinte = Cliente.objects.get(pk=cliente_id)
    Cleinte.delete()
    return redirect('clientes')

def emprestimo(request, caixa_cod, cliente_cod):
    Caixa = Caixa.objects.get(codCaixa=caixa_cod)
    Cliente = Cliente.objects.get(codCliente=cliente_cod)
    CaixaClienteobj = CaixaCliente(idCliente=Cliente.id, idCaixa = Caixa.id)
    CaixaClienteobj.save()
    
    return redirect('main')