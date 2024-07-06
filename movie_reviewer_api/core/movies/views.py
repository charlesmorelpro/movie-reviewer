from django.shortcuts import render
from rest_framework import generics

from core.movies.models import Movie
from core.movies.serializers import (MovieDetailsSerializer, MovieSerializer,
                                     MovieUpdateSerializer)


class MoviesView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailsView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailsSerializer


class MovieUpdateView(generics.UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieUpdateSerializer
