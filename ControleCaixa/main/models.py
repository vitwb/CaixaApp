from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
class Cliente (models.Model):
    id = models.BigAutoField(primary_key=True)
    nomeCliente = models.CharField(max_length=200)
    codCliente = models.CharField(max_length=10)
    dataCadastroCliente = models.DateTimeField(auto_now_add=True, blank=True)
    qr_code_cl =models.ImageField(upload_to='qrcodescl',blank=True)
    def __str__(self):
            return f"{self.nomeCliente},{self.codCliente},{self.dataCadastroCliente},"
    
    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.codCliente)
        canvas = Image.new('RGB', (290, 290), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.codCliente}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code_cl.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
    
class Caixa (models.Model):
    id = models.BigAutoField(primary_key=True)
    codCaixa = models.CharField(max_length=10)
    dataCadastroCaixa = models.DateTimeField(auto_now_add=True, blank=True)
    qr_code_cx =models.ImageField(upload_to='qrcodescx',blank=True)
    def __str__(self):
            return f"{self.codCaixa},{self.dataCadastroCaixa},"
    
    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.codCaixa)
        canvas = Image.new('RGB', (290, 290), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.codCaixa}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code_cx.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
    
class CaixaCliente (models.Model):
    idCliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    idCaixa = models.ForeignKey(Caixa, on_delete=models.DO_NOTHING)  
    dataEmprestimo = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
            return f"{self.idCliente},{self.idCaixa},{self.dataEmprestimo}"