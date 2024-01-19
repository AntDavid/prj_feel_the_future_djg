from django.contrib import admin
from . models import Categoria, Flashcard, Challenge, FlashcardChallenge

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Flashcard)
admin.site.register(Challenge)
admin.site.register(FlashcardChallenge)
