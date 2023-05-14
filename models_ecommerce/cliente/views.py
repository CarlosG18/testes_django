from django.shortcuts import render
from .models import Cliente
from produto.models import Produto

def index(request):
  return render(request, "cliente/index.html")
  
def save(request):
  produtos = Produto.objects.all()
  if request.method == "GET":
    return render(request, "cliente/home.html", {
      "produtos": produtos,
    })
  elif request.method == "POST":
    nome = request.POST["nome"]
    email = request.POST["email"]
    cpf = request.POST["cpf"]
    cliente = Cliente(nome=nome,email=email,cpf=cpf)
    cliente.save()
    return render(request, "cliente/home.html", {
    "cliente": cliente,
    "produtos": produtos,
    })

