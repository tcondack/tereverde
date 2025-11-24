from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from .models import Parque, Trilhas, Eventos
from bson import ObjectId


# Página de teste
def teste(request):
    return render(request, 'myapp/teste.html')


# Páginas públicas

def index(request):
    parques = Parque.objects.all()[:3]  # Mostra os 3 primeiros parques

    contexto = {
        'parques': parques,
        'trilhas': trilhas,
        'eventos': eventos
    }

    return render(request, 'myapp/index.html', contexto)


def parques(request):
    parques = Parque.objects.all()
    return render(request, 'myapp/parques.html', {'parques': parques})


def trilhas(request, parque_id=None):
    if parque_id:
        trilhas = Trilhas.objects.filter(parque_id=ObjectId(parque_id))
    else:
        lista_trilhas = Trilhas.objects.all()
    return render(request, 'myapp/trilhas.html', {'parque': parques, 'trilhas': lista_trilhas})


def eventos(request, parque_id=None):
    if parque_id:
        eventos = Eventos.objects.filter(parque_id=ObjectId(parque_id))
    else:
        eventos = Eventos.objects.all()
        return render(request, 'myapp/eventos.html', {'eventos': eventos})


# Páginas de cadastro
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'myapp/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha_confirmacao = request.POST.get('senha_confirmacao')  # Captura o novo campo

        # 1. Verificar se as senhas coincidem
        if senha != senha_confirmacao:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('cadastro')

        # Verifica se existe usuário com o mesmo nome
        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('Usuário já cadastrado')

        # cria e salva o novo usuário
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return HttpResponse('Usuário cadastrado com sucesso!')


# Login  usuário
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        user = authenticate(username=username, password=senha)

        if user is not None and user.is_staff:
            login_django(request, user)
            return redirect('/admin/')
        else:
            messages.error(request, 'Credenciais inválidas ou usuário sem permissão de acesso.')

    return render(request, 'myapp/login.html')


@login_required(login_url='/auth/login/')
def admin(request):
    return HttpResponse('Acesso liberado, Página protegida')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))