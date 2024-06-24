from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django, logout
from django.contrib.auth.decorators import login_required
from .models import Reuniao
from .forms import ReuniaoForm

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('login')
        email = request.POST.get('email')
        password = request.POST.get('senha')

        if not username or not email or not password:
            return HttpResponse("Todos os campos são obrigatórios.")

        if User.objects.filter(username=username).exists():
            return HttpResponse("Nome de usuário já existente.")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return HttpResponse("Usuário cadastrado com sucesso!")

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('login')
        password = request.POST.get('senha')

        user = authenticate(username=username, password=password)

        if user is not None:
            login_django(request, user)
            return redirect('listar_reunioes')
        else:
            return HttpResponse("Nome de usuário ou senha inválidos.")

@login_required(login_url="/auth/login/")
def listar_reunioes(request):
    reunioes = Reuniao.objects.filter(usuario=request.user)
    return render(request, 'listar_reunioes.html', {'reunioes': reunioes})

@login_required(login_url="/auth/login/")
def adicionar_reuniao(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        data = request.POST.get('data')
        hora_inicio = request.POST.get('hora_inicio')
        hora_fim = request.POST.get('hora_fim')
        descricao = request.POST.get('descricao')

        Reuniao.objects.create(
            titulo=titulo,
            data=data,
            hora_inicio=hora_inicio,
            hora_fim=hora_fim,
            descricao=descricao,
            usuario=request.user
        )
        return redirect('listar_reunioes')
    return render(request, 'adicionar_reuniao.html')

@login_required(login_url="/auth/login/")
def editar_reuniao(request, id):
    reuniao = Reuniao.objects.get(id=id)

    if request.method == "POST":
        reuniao.titulo = request.POST.get('titulo')
        reuniao.data = request.POST.get('data')
        reuniao.hora_inicio = request.POST.get('hora_inicio')
        reuniao.hora_fim = request.POST.get('hora_fim')
        reuniao.descricao = request.POST.get('descricao')
        reuniao.save()
        return redirect('listar_reunioes')
    return render(request, 'editar_reuniao.html', {'reuniao': reuniao})

@login_required(login_url="/auth/login/")
def excluir_reuniao(request, id):
    reuniao = get_object_or_404(Reuniao, id=id, usuario=request.user)
    reuniao.delete()
    return redirect('listar_reunioes')

def logout_view(request):
    logout(request)
    return redirect('login')