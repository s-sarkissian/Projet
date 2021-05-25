from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=200)
    subscribers = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Priorite(models.Model):
    label = models.CharField(max_length=200)

    def __str__(self):
        return self.label


class Post(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_creation = models.DateTimeField()
    community = models.ForeignKey(Community, on_delete='CASCADE')
    priorite = models.ForeignKey(Priorite, on_delete='CASCADE')
    evenementiel = models.BooleanField()
    date_evenement = models.DateField()
    auteur = models.ForeignKey(User, on_delete='CASCADE')

    def __str__(self):
        return self.titre


class Comment(models.Model):
    date_creation = models.DateTimeField()
    contenu = models.TextField()
    auteur = models.ForeignKey(User, on_delete='CASCADE')
    post = models.ForeignKey(Post, on_delete='CASCADE')

    def __str__(self):
        return self.auteur.username
