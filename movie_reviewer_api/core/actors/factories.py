import factory

from core.actors.models import Actor


class ActorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Actor

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
