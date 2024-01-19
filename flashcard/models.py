from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Flashcard(models.Model):
    DIFICULDADE_CHOICES = (('D', 'Difícil'), ('M', 'Médio'), ('F', 'Fácil'))
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    question = models.CharField(max_length=100)
    resp = models.TextField()
    category = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    difficulty = models.CharField(max_length=1, choices=DIFICULDADE_CHOICES)

    def __str__(self):
        return self.question

class FlashcardChallenge(models.Model):
    flashcard = models.ForeignKey(Flashcard, on_delete=models.DO_NOTHING)
    answered = models.BooleanField(default=False)
    nailed_it = models.BooleanField(default=False)

    def __str__(self):
        return self.flashcard.question


class Challenge(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    tittle = models.CharField(max_length=100)
    category = models.ManyToManyField(Categoria)
    quantity_questions = models.IntegerField()
    difficulty = models.CharField(
        max_length=1, choices=Flashcard.DIFICULDADE_CHOICES
    )
    flashcards = models.ManyToManyField(FlashcardChallenge)

    def __str__(self):
        return self.tittle
