import logging

from core.actors.models import Actor
from core.movies.models import Movie
from core.reviews.models import Review

logger = logging.getLogger(__name__)


def clean_all_database():
    logger.info("Clean all database")
    Review.objects.all().delete()
    Movie.objects.all().delete()
    Actor.objects.all().delete()
    logger.info("All database cleaned")
