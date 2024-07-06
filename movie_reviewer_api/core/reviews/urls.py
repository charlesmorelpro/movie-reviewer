from django.urls import path

from core.reviews import views

urlpatterns = [
    path("", views.ReviewCreateView.as_view()),
]
