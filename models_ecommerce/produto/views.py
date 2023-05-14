from django.shortcuts import render
from .models import Produto
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):
  return render(request, "produto/index.html")
  
def save(request):
  cod = request.POST["codigo"]
  nome = request.POST["nome"]
  price = request.POST["price"]
  descricao = request.POST["descricao"]
  produto = Produto(codigo=cod,nome=nome,price=price,descricao=descricao)
  produto.save()
  #return render(request, "cliente/index.html")
  return HttpResponseRedirect(reverse('cliente:index'))