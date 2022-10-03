from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=3)
    owner = models.CharField(max_length=100)

    def __str__(self):
        return self.name
