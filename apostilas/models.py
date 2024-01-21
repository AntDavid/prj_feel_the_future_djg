from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Handout(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    tittle = models.CharField(max_length=100)
    file = models.FileField(upload_to='apostilas')

    def __str__(self):
        return self.tittle

class ViewHandout(models.Model):
    ip = models.GenericIPAddressField()
    handout = models.ForeignKey(Handout, on_delete=models.DO_NOTHING)


    def __STR__(self):
        return self.ip
