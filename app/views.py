from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib.auth import login, logout
from .models import Produto
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')
    
def cadastro(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('login') # Redireciona para a página de login após o cadastro
        else:
             messages.error(request, 'Erro ao cadastrar usuário. Verifique os dados.')
    else:
        form = UserForm()

    context = {
        'form': form
    }
    return render(request, 'cadastro.html', context)



def login_(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            messages.success(request, 'Login efetuado com sucesso!')
            return redirect('main', id=user.id) # Redireciona para a página principal
        else:
           messages.error(request, "Erro ao fazer o login, confira suas credenciais")
    else:
        form = LoginForm()

    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def logout_(request):
    logout(request)
    messages.success(request, "Logout efetuado com sucesso")
    return redirect('login')

@login_required
def main(request, id):
    NUMBER = 10
    produtos = Produto.objects.all()

    if request.user.id != int(id):  
        return redirect('login')  # Redirecione para a página de login
    
    context = {
        'NUMBER': NUMBER,
        'produtos': produtos
    }
    for produto in produtos:
        print(produto.nome)
        
    return render(request, 'main.html', context) # Corrigido, passando o contexto para o template