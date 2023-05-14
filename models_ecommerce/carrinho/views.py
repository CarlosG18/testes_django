from django.shortcuts import render
from .models import Carrinho, ItemCarrinho
from cliente.models import Cliente
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect

def create(request, pk):
  cliente = Cliente.objects.filter(pk=pk).get()
  carrinho = Carrinho(cliente=cliente)
  carrinho.save()
  return HttpResponseRedirect(reverse('cliente:home'))