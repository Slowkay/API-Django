from django.db import models


class Exercice(models.Model):
    # nom_exo, poids, tmp_repos, repetitions, series
    name = models.CharField(max_length=100)
    weight = models.PositiveSmallIntegerField()
    seconds_rest_time = models.PositiveSmallIntegerField()
    rehearsals = models.PositiveSmallIntegerField()
    series = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
