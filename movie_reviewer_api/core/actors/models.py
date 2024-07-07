import uuid

from django.db import models


class Actor(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name
