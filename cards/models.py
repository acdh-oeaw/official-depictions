from django.db import models
from vocabs.models import SkosConcept
from entities.models import Person
from entities.models import Institution
from entities.validators import date_validator
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
    artist = models.ManyToManyField(Person, blank=True, related_name='card_creator')
    reference = models.ManyToManyField(Book, blank=True)
    published_written = models.CharField(
        max_length=255, blank=True, null=True,
        validators=[date_validator, ],
        help_text="Please enter a date (DD).(MM).YYYY")
    published = models.DateField(blank=True, null=True)
    run_written = models.CharField(
        max_length=255, blank=True, null=True,
        validators=[date_validator, ],
        help_text="Please enter a date (DD).(MM).YYYY")
    hosting_institution = models.ManyToManyField(Institution, blank=True)
    note = models.TextField(blank=True, null=True)
    reference = models.ManyToManyField(Book, blank=True)
    mentioned_work = models.ManyToManyField(Book, blank=True, related_name='mentioned_work')
    mentioned_person = models.ManyToManyField(
        Person, blank=True, related_name='mentioned_person'
    )
    mentioned_person = models.ManyToManyField(
        Institution, blank=True, related_name='mentioned_institution'
    )
    mentioned_concept = models.ManyToManyField(
        SkosConcept, blank=True, related_name='mentioned_concept'
    )
