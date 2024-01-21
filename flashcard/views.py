from django.shortcuts import render, redirect
from . models import Categoria, Flashcard, Challenge, FlashcardChallenge
from django.contrib.messages import constants
from django.contrib import messages
from django.http import HttpResponse, Http404


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
    if (request.method == "GET"):
        categorias = Categoria.objects.all()
        dificuldades = Flashcard.DIFICULDADE_CHOICES
        return render(request, 'iniciar_desafio.html/', {'categorias': categorias,
                                                        'dificuldades': dificuldades})

    elif (request.method == "POST"):
        form_tittle = request.POST.get('titulo')
        form_category = request.POST.getlist('categoria')
        form_difficulty = request.POST.get('dificuldade')
        form_quantity_questions = request.POST.get('qtd_perguntas')


    challenge = Challenge(
        user=request.user,
        tittle = form_tittle,
        difficulty = form_difficulty,
        quantity_questions = form_quantity_questions
    )

    challenge.save()



    for item in form_category:
        challenge.category.add(item)

    flashcards = (Flashcard.objects.filter(user=request.user)
                .filter(difficulty=form_difficulty)
                .filter(category_id__in=form_category)
                .order_by('?')
                )

    if (flashcards.count() < int(form_quantity_questions)):
        messages.add_message(request, constants.ERROR, 'error')
        return redirect('/flashcard/iniciar_desafio/')

    flashcards = flashcards[: int(form_quantity_questions)]

    for flash in flashcards:
        flashcard_desafio = FlashcardChallenge(
            flashcard = flash
        )
        flashcard_desafio.save()
        challenge.flashcards.add(flashcard_desafio)
    return redirect('/flashcard/listar_desafio/')

def listar_desafio(request):
    challenge = Challenge.objects.filter(user=request.user)
    return render(request, 'listar_desafio.html', {'desafios': challenge})

def desafio(request, id):
    desafio = Challenge.objects.get(id=id)
    if (not desafio.user == request.user):
        raise Http404

    if(request.method == "GET"):
        nailed_it = desafio.flashcards.filter(answered=True).filter(nailed_it=True).count()
        not_nailed_it = desafio.flashcards.filter(answered=True).filter(nailed_it=False).count()
        missing = desafio.flashcards.filter(answered=False).count()
        return render(request, 'desafio.html', {'desafio': desafio,
                                                'nailed_it': nailed_it,
                                                'not_nailed_it': not_nailed_it,
                                                'missing': missing})


def responder_flashcard(request, id):
    flash_challenge = FlashcardChallenge.objects.get(id=id)
    got_it_right = request.GET.get('nailed_it')
    challenge_id = request.GET.get('challenge_id')

    if (not flash_challenge.flashcard.user == request.user):
        raise Http404()

    flash_challenge.answered = True

    flash_challenge.nailed_it = True if got_it_right == "1" else False
    flash_challenge.save()

    return redirect(f'/flashcard/desafio/{challenge_id}')


def relatorio(request, id):
    desafio = Challenge.objects.get(id=id)
    acertos = desafio.flashcards.filter(nailed_it=True).count()
    erros = desafio.flashcards.filter(nailed_it=False).count()
    data_one = [acertos, erros]

    category = desafio.category.all()

    name_category = [i.nome for i in category]

    print(category)
    print(name_category)
    data_two = []
    for categoria in category:
        data_two.append(desafio.flashcards.filter(flashcard__category=categoria).filter(nailed_it=True).count() )

    print(data_two)



    return render(request, 'relatorio.html', {'desafio':desafio, 'data_one':data_one, 'name_category':name_category, 'data_two':data_two})



