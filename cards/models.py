from django.db import models
from django.utils.text import Truncator
from vocabs.models import SkosConcept
from entities.models import Person, Institution, Event
from entities.models_base import match_date
from entities.validators import date_validator
from bib.models import Book


class Collection(models.Model):
    """ Describebes a series of cards """

    name = models.CharField(max_length=250, blank=True)
    abbreviation = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return "{}".format(self.abbreviation)


class Card(models.Model):
    """This class describes a post-card like entity"""

    title = models.CharField(max_length=250, blank=True)
    legacy_id = models.CharField(max_length=25, blank=True)
    collection = models.ForeignKey(Collection, blank=True, null=True)
    descriptions = models.TextField(blank=True)
    lenght = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    scan_front = models.ImageField(blank=True, null=True)
    scan_back = models.ImageField(blank=True, null=True)
    text_front = models.TextField(blank=True)
    text_back = models.TextField(blank=True)
    printing_method = models.ForeignKey(SkosConcept, blank=True, null=True)
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
    run = models.DateField(blank=True, null=True)
    hosting_institution = models.ManyToManyField(Institution, blank=True)
    note = models.TextField(blank=True, null=True)
    reference = models.ManyToManyField(Book, blank=True)
    mentioned_work = models.ManyToManyField(Book, blank=True, related_name='mentioned_work')
    mentioned_person = models.ManyToManyField(
        Person, blank=True, related_name='mentioned_person'
    )
    mentioned_institution = models.ManyToManyField(
        Institution, blank=True, related_name='mentioned_institution'
    )
    mentioned_concept = models.ManyToManyField(
        SkosConcept, blank=True, related_name='mentioned_concept'
    )
    mentioned_event = models.ManyToManyField(
        Event, blank=True, related_name='mentioned_event'
    )
    public = models.BooleanField(default=False)

    def __str__(self):
        return "{}, {}: '{}'".format(
            self.collection, self.legacy_id,
            Truncator(self.title).chars(25)
        )

    def save(self, *args, **kwargs):
        """Adaption of the save() method of the class to automatically parse string-dates into date objects
        """
        if self.published_written:
            self.published, self.published_written = match_date(self.published_written)
        if self.run_written:
            self.run, self.run_written = match_date(self.run_written)
        super(Card, self).save(*args, **kwargs)
        return self
