from django import forms

class MyForms(forms.Form):
    imagem = forms.ImageField()