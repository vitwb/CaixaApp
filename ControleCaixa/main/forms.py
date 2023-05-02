from django import forms


class FormsCaixa(forms.Form):
    codCaixa = forms.CharField(max_length=10)