from django.db import models
from django.db.models.fields import DateTimeField
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


# Create your models here.
class Netfeelex(models.Model):
    # CharFiels pour mettre une restriction
    Titre_film = models.CharField(max_length=200)
    Contenu_film = models.TextField()
    Date_publication = models.DateTimeField("Date publié", default=datetime.now())
    category = models.ForeignKey(
        Category, related_name='netfeelex', on_delete=models.CASCADE, default='')

    # fonction de recuperation
    def __str__(self):
        return self.Titre_film


"""class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    def __str__(self):
        return self.username"""
