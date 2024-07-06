import factory

from core.actors.factories import ActorFactory
from core.movies.models import Movie


class MovieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Movie

    id = factory.Faker("uuid4")
    title = factory.Faker("sentence", nb_words=4)
    description = factory.Faker("text")

    @factory.post_generation
    def actors(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for actor in extracted:
                self.actors.add(actor)
        else:
            actors = ActorFactory.create_batch(5)
            self.actors.add(*actors)
