import uuid

from django.db import models


class Actor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField()
    last_name = models.CharField()
