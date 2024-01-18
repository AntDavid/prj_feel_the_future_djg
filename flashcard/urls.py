from django.urls import path
from . import views

urlpatterns = [
    path('novo_flashcard/', views.novo_flashcard, name="novo_flashcard"),
    path('deletar_flashcard/<int:id>', views.deletar_flashcard, name="deletar_flashcard")
]
