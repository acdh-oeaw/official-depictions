from django.db import models


class Person(models.Model):
    """ Describes some person like entity """

    forename = models.CharField(max_length=250, blank=True)
    surname = models.CharField(max_length=250, blank=True)
