from django.db import models

class Cliente (models.Model):
    id = models.BigAutoField(primary_key=True)
    nomeCliente = models.CharField(max_length=200)
    dataCadastroCliente = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
            return f"{self.nomeCliente},{self.dataCadastroCliente},"
    
class Caixa (models.Model):
    id = models.BigAutoField(primary_key=True)
    codCaixa = models.CharField(max_length=10)
    dataCadastroCaixa = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
            return f"{self.codCaixa},{self.dataCadastroCaixa},"
    
class CaixaCliente (models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    idCaixa = models.ForeignKey(Caixa, on_delete=models.DO_NOTHING)  
    dataEmprestimo = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
            return f"{self.idCliente},{self.idCaixa},{self.dataEmprestimo}"