from django.shortcuts import render
from .models import Carrinho, ItemCarrinho
from cliente.models import Cliente
from produto.models import Produto
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect

def create(request, pk):
  produtos = Produtos.objects.all()
  cliente = Cliente.objects.filter(pk=pk).get()
  carrinho = Carrinho(cliente=cliente)
  carrinho.save()
  return render(request, "carrinho/index.html", {
    "Cliente": cliente,
    "produtos": Produtos,
  })
  
def add(request, pk):
  return HttpResponse(pk)