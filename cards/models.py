from django.db import models
from django.utils.text import Truncator
from vocabs.models import SkosConcept
from entities.models import Person, Institution, Place, Event
from bib.models import Book
from images.models import Image
from idprovider.models import IdProvider


class CardCollection(IdProvider):
    """ Describebes a series of cards """

    name = models.CharField(max_length=250, blank=True)
    abbreviation = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return "{}".format(self.abbreviation)


class Card(IdProvider):
    """This class describes a post-card like entity"""

    title = models.CharField(max_length=250, blank=True)
    legacy_id = models.CharField(max_length=25, blank=True)
    card_collection = models.ForeignKey(CardCollection, blank=True, null=True)
    descriptions = models.TextField(blank=True)
    lenght = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    scan_front = models.ForeignKey(Image, blank=True, null=True, related_name="front_image_of")
    scan_back = models.ForeignKey(Image, blank=True, null=True, related_name="back_image_of")
    text_front = models.TextField(blank=True)
    text_back = models.TextField(blank=True)
    printing_method = models.ForeignKey(SkosConcept, blank=True, null=True)
    artist = models.ManyToManyField(Person, blank=True, related_name='card_creator')
    reference = models.ManyToManyField(Book, blank=True)
    published_written = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="Please enter a date (DD).(MM).YYYY")
    published = models.DateField(blank=True, null=True)
    run_written = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="Please enter a date (DD).(MM).YYYY")
    run = models.DateField(blank=True, null=True)
    hosting_institution = models.ManyToManyField(Institution, blank=True)
    note = models.TextField(blank=True, null=True)
    reference = models.ManyToManyField(Book, blank=True)
    mentioned_work = models.ManyToManyField(Book, blank=True, related_name='mentioned_work')
    mentioned_person = models.ManyToManyField(
        Person, blank=True, related_name='mentioned_person'
    )
    mentioned_place = models.ManyToManyField(
        Place, blank=True, related_name='mentioned_place'
    )
    mentioned_institution = models.ManyToManyField(
        Institution, blank=True, related_name='mentioned_institution'
    )
    mentioned_concept = models.ManyToManyField(
        SkosConcept, blank=True, related_name='mentioned_concept'
    )
    mentioned_place = models.ManyToManyField(
        Event, blank=True, related_name='mentioned_event'
    )
    public = models.BooleanField(default=False)

    def __str__(self):
        return "{}, {}: '{}'".format(
            self.collection, self.legacy_id,
            Truncator(self.title).chars(25)
        )
