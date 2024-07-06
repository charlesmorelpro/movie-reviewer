import logging

from django.core.management import base

from core.actors.factories import ActorFactory
from core.movies.factories import MovieFactory
from movie_reviewer_api.scripts.clean_all_database import clean_all_database

logger = logging.getLogger(__name__)


class Command(base.BaseCommand):
    help = "Create a testing dataset"

    def handle(self, *args, **options):
        clean_all_database()

        logger.info("Create movies")
        MovieFactory.create_batch(10)
