from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth


def cadastro(request):

    if (request.method == "GET"):
        return render(request, 'cadastro.html')
    elif (request.method == "POST"): 

        form_username = request.POST.get('username')
        form_password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if (not form_password == confirm_password):
            messages.add_message(request, constants.ERROR, 'Senhas não coincidem!')
            return redirect ('/usuarios/cadastro')
        
        user = User.objects.filter(username = form_username)
        
        if (user.exists()):
          messages.add_message(request, constants.ERROR, 'Usuário já existe!')
          return redirect('/usuarios/cadastro')

        try:
            User.objects.create_user(
                username=form_username,
                password=form_password
            )
            return  redirect('/usuarios/logar')
        
        except:
          messages.add_message(request, constants.ERROR, 'erro interno do servidor')
          return redirect('/usuarios/cadastro')
        

def logar(request):
    if (request.method == "GET"):
      return render(request, 'login.html')
   
    elif (request.method == "POST"):
       form_username = request.POST.get('username')
       form_password = request.POST.get('password')

       user = auth.authenticate(request, username=form_username, password=form_password)

       if user:
          auth.login(request, user)
          messages.add_message(request, constants.SUCCESS, 'Logado com sucesso!')
          return redirect('/flashcards/new_flashcards/')
       
       else:
          messages.add_message(request, constants.ERROR, 'Username ou passoword inválido!')
          return redirect('/usuarios/logar/')


def logout(request):
   auth.logar(request)
   return redirect ('/usuarios/login/')
