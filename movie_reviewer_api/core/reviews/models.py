import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.movies.models import Movie


class Review(models.Model):
    grade = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
