from django.db import models
from vocabs.models import SkosConcept
from persons.models import Person
from bib.models import Book


class Collection(models.Model):
    """ Describebes a series of cards """

    name = models.CharField(max_length=250, blank=True)
    abbreviation = models.CharField(max_length=25, blank=True)


class Card(models.Model):
    """This class describes a post-card like entity"""

    legacy_id = models.CharField(max_length=25, blank=True)
    collection = models.ForeignKey(Collection, blank=True)
    descriptions = models.TextField(blank=True)
    lenght = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    scan_front = models.ImageField(null=True)
    scan_back = models.ImageField(null=True)
    text_front = models.TextField(blank=True)
    text_back = models.TextField(blank=True)
    printing_method = models.ForeignKey(SkosConcept, blank=True)
    artist = models.ManyToManyField(Person, blank=True)
    reference = models.ManyToManyField(Book, blank=True)
