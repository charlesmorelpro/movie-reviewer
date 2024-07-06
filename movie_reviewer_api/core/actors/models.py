import uuid

from django.db import models


class Actor(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
