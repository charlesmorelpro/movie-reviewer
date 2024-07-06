import uuid

from django.db import models

from core.actors.models import Actor


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField()
    description = models.TextField()
    actors = models.ManyToManyField(Actor)
