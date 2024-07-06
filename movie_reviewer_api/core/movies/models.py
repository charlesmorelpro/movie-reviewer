import uuid

from django.db import models

from core.actors.models import Actor


class Movie(models.Model):
    title = models.CharField()
    description = models.TextField()
    actors = models.ManyToManyField(Actor)
