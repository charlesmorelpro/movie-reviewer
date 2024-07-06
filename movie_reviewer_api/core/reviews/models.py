import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.movies.models import Movie


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    grade = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
