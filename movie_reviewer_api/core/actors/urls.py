from django.urls import path

from core.actors import views

urlpatterns = [
    path("", views.ActorsView.as_view(), name="actors"),
]
