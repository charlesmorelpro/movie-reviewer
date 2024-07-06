import factory

from core.actors.models import Actor


class ActorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Actor

    id = factory.Faker("uuid4")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
