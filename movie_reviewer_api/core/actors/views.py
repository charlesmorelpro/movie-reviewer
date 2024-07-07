from rest_framework import generics

from core.actors.models import Actor
from core.actors.serializers import ActorSerializer


class ActorsView(generics.ListAPIView):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all().order_by("first_name")
    pagination_class = None
