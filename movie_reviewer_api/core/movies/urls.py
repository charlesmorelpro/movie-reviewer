from django.urls import path

from core.movies import views

urlpatterns = [
    path("", views.MoviesView.as_view(), name="movies"),
    path("<int:pk>/", views.MovieDetailsView.as_view(), name="movie-details"),
    path("<int:pk>/update/", views.MovieUpdateView.as_view(), name="movie-update"),
]
