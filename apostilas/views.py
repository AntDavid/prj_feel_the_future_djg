from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from . models import Handout, ViewHandout
from django.contrib.messages import constants
from django.contrib import messages
# Create your views here.

def adicionar_apostilas(request):
    if (request.method == "GET"):
        apostilas = Handout.objects.filter(user=request.user)

        all_views = ViewHandout.objects.filter(handout__user=request.user).count()
        return render(request, 'adicionar_apostilas.html', {'apostilas':apostilas, 'views_totais':all_views})

    elif (request.method == "POST"):
        form_tittle = request.POST.get('tittle')
        form_file = request.FILES['file']

        """if (form_tittle == "") or len(request.FILES) is not 0:
            messages.add_message(request, constants.ERROR, "Campos vazios não são aceitos!")
            raise Http404"""

        hand = Handout(
            user = request.user,
            tittle  = form_tittle,
            file = form_file
        )

        hand.save()
        messages.add_message(request, constants.SUCCESS, "Salvo com sucesso!")
        return redirect('/apostilas/adicionar_apostilas')


def apostila(request, id):
    apostila = Handout.objects.get(id=id)
    all_views = ViewHandout.objects.filter(handout=apostila).count
    single_view = ViewHandout.objects.filter(handout=apostila).values('ip').distinct().count
    view = ViewHandout(
        ip=request.META['REMOTE_ADDR'],
        handout=apostila
    )
    view.save()
    return render(request, 'apostila.html', {'apostila':apostila, 'all_views':all_views, 'single_view':single_view})

