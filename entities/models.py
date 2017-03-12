from django.db import models
from .models_base import TempEntityClass
from places.models import Place
from vocabs.models import SkosConcept


class Event(TempEntityClass):
    kind = models.ManyToManyField(SkosConcept, blank=True)
    located_in = models.ForeignKey(Place, blank=True, null=True)


class Institution(TempEntityClass):
    kind = models.ManyToManyField(SkosConcept, blank=True)
    homepage = models.URLField(blank=True, null=True)
    address = models.CharField(blank=True, max_length=250)
    located_in = models.ForeignKey(Place, blank=True, null=True)

    def __str__(self):
        return self.name


class Person(TempEntityClass):
    """ A temporalized entity to model a human beeing."""

    GENDER_CHOICES = (('female', 'female'), ('male', 'male'))
    first_name = models.CharField(
        max_length=255,
        help_text='The persons´s forename. In case of more then one name...',
        blank=True,
        null=True)
    born_in = models.ForeignKey(Place, blank=True, null=True, related_name='birth_place')
    died_in = models.ForeignKey(Place, blank=True, null=True, related_name='death_place')
    profession = models.ManyToManyField(
        SkosConcept, blank=True, related_name='profession')
    title = models.ManyToManyField(SkosConcept, blank=True, related_name='title')
    gender = models.CharField(
        max_length=15, choices=GENDER_CHOICES,
        blank=True)

    def __str__(self):
        if self.first_name != "" and self.name != "":
            return "{}, {}".format(self.name, self.first_name)
        elif self.first_name != "" and self.name == "":
            return "{}, {}".format("no surename provided", self.first_name)
        elif self.first_name == "" and self.name != "":
            return self.name
        elif self.first_name == "" and self.name == "":
            return "no name provided"
