from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from .models import Parque, Trilhas, Eventos
from .serializers import ParqueSerializer, TrilhasSerializer, EventosSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Página de teste
def teste(request):
    return render(request, 'myapp/teste.html')


# Páginas públicas


## Parques 
def index(request):
    parques = Parque.objects.all()[:3]  # Mostra os 3 primeiros parques
    contexto = {
        'parques': parques,
    }
    return render(request, 'myapp/index.html', contexto)

def parques(request):
    parques = Parque.objects.all()
    return render(request, 'myapp/parques.html', {'parques': parques})

def parque_create(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        localizacao = request.POST.get('localizacao')
        horario_funcionamento = request.POST.get('horario_funcionamento')
        ativo = request.POST.get('ativo') == 'on'  # Checkbox handling

        parque = Parque.objects.create(
            nome=nome,
            descricao=descricao,
            localizacao=localizacao,
            horario_funcionamento=horario_funcionamento,
            ativo=ativo
        )
        return redirect('parques')  # redireciona para a lista de parques depos de criar
    return render(request, 'myapp/parque_create.html')

def parque_update(request, parque_id):
    parque = get_object_or_404(Parque, id=parque_id)
    if request.method == 'POST':
        parque.nome = request.POST.get('nome')
        parque.descricao = request.POST.get('descricao')
        parque.localizacao = request.POST.get('localizacao')
        parque.horario_funcionamento = request.POST.get('horario_funcionamento')
        parque.ativo = request.POST.get('ativo') == 'on'  # Checkbox handling
        parque.save()
        return redirect('parques')  # redireciona para a lista de parques depois de atualizar
    return render(request, 'myapp/parque_update.html', {'parque': parque})

def parque_delete(request, parque_id):
    parque = get_object_or_404(Parque, id=parque_id)
    if request.method == 'POST':
        parque.delete()
        return redirect('parques')  # redireciona para a lista de parques depois de deletar
    return render(request, 'myapp/parque_delete.html', {'parque': parque})


@api_view(['GET'])
def parques_api(request):
    parques  = Parque.objects.all()
    serializer = ParqueSerializer(parques, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


## Trilhas

def trilhas(request, parque_id=None):
    if parque_id:
        trilhas = Trilhas.objects.filter(parque_id=int(parque_id))
    else:
        lista_trilhas = Trilhas.objects.all()
    return render(request, 'myapp/trilhas.html', {'parque': parques, 'trilhas': lista_trilhas})


@api_view(['GET'])
def trilhas_api(request):
    trilhas  = Trilhas.objects.all()
    serializer = TrilhasSerializer(trilhas, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def eventos(request, parque_id=None):
    if parque_id:
        eventos = Eventos.objects.filter(parque_id=int(parque_id))
    else:
        eventos = Eventos.objects.all()
        return render(request, 'myapp/eventos.html', {'eventos': eventos})

@api_view(['GET'])
def eventos_api(request):
    eventos  = Eventos.objects.all()
    serializer = EventosSerializer(eventos, many=True)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)


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

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))