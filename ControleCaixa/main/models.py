from django.db import models

class Cliente (models.Model):
    id = models.BigAutoField(primary_key=True)
    nomeCliente = models.CharField(max_length=200)

    def __str__(self):
            return f"{self.nomeCliente},"
    
class Caixa (models.Model):
    id = models.BigAutoField(primary_key=True)
    codCaixa = models.CharField(max_length=10)

    def __str__(self):
            return f"{self.codCaixa},"
    
class CaixaCliente (models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    idCaixa = models.ForeignKey(Caixa, on_delete=models.DO_NOTHING)  
    def __str__(self):
            return f"{self.idCliente},{self.idCaixa}"