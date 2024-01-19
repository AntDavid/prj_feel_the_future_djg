from django.shortcuts import render, redirect
from . models import Categoria, Flashcard
from django.contrib.messages import constants
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.

def novo_flashcard(request):
    if (not request.user.is_authenticated):
        return redirect('/usuarios/logar')

    if (request.method == "GET"):
        categorias = Categoria.objects.all()
        dificuldades = Flashcard.DIFICULDADE_CHOICES
        flashcard_list = Flashcard.objects.filter(user=request.user)
        return render(request, 'novo_flashcard.html', {'categorias': categorias,
                                                       'dificuldades':dificuldades,
                                                       'flashcards': flashcard_list})

    elif (request.method == "POST"):
        form_pergunta = request.POST.get('pergunta')
        form_resposta = request.POST.get('resposta')
        form_categoria = request.POST.get('categoria')
        form_dificuldade = request.POST.get('dificuldade')

        if (len(form_pergunta.strip()) == 0 or len(form_resposta.strip()) == 0):
            messages.add_message(request, constants.ERROR, "Proibido enviar campos em branco!")
            return redirect('/flashcard/novo_flashcard/')


        flashcard = Flashcard (
            user = request.user,
            question  = form_pergunta,
            resp = form_resposta,
            difficulty = form_dificuldade,
            category_id = form_categoria
        )


        flashcard.save()
        messages.add_message(request, constants.SUCCESS, "Flashcard adicionado com sucesso!")
        return redirect('/flashcard/novo_flashcard/')


def deletar_flashcard(request, id):
    flashcard_to_delete = Flashcard.objects.get(id=id)

    if (flashcard_to_delete.user == request.user):
        flashcard_to_delete.delete()
        messages.add_message(request, constants.SUCCESS, 'Deletado com sucesso!')
    else:
        messages.add_message(request, constants.ERROR, 'Erro ao deletar')
    return redirect('/flashcard/novo_flashcard/')


def iniciar_desafio(request):
    if request.method == "GET":
        categorias = Categoria.objects.all()
        dificuldades = Flashcard.DIFICULDADE_CHOICES
        return render(request, 'iniciar_desafio.html/', {'categorias': categorias,
                                                        'dificuldades': dificuldades})
