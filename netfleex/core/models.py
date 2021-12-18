from django.db import models
from django.db.models.fields import DateTimeField
from datetime import datetime

# Create your models here.
class Netfeelex(models.Model):
    #CharFiels pour mettre une restriction
    Titre_film = models.CharField(max_length=200)
    Contenu_film = models.TextField()
    Date_publication = models.DateTimeField("Date publié", default = datetime.now())
    Category = models.CharField(max_length=200)
    #fonction de recuperation
    def __str__(self):
        return self.Titre_film
class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
"""class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    def __str__(self):
        return self.username"""