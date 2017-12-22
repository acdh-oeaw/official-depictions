from django.db import models
from django.core.urlresolvers import reverse
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

    def get_next(self):
        next = CardCollection.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = CardCollection.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def get_absolute_url(self):
        return reverse('cards:cardcol_detail', kwargs={'pk': self.id})

    @classmethod
    def get_listview_url(self):
        return reverse('browsing:browse_cardcollections')

    @classmethod
    def get_createview_url(self):
        return reverse('cards:cardcol_create')


class Card(IdProvider):
    """This class describes a post-card like entity"""

    title = models.CharField(max_length=250, blank=True, verbose_name="Bildquelle")
    legacy_id = models.CharField(max_length=25, blank=True, verbose_name="Lfd. Nr.")
    number = models.CharField(max_length=25, blank=True, verbose_name="Nr (Serie)")
    card_collection = models.ForeignKey(
        CardCollection, blank=True, null=True, verbose_name="Serienkürzel",
        related_name="conain_cards"
    )
    descriptions = models.TextField(blank=True)
    lenght = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    scan_front = models.ForeignKey(Image, blank=True, null=True, related_name="front_image_of")
    scan_back = models.ForeignKey(Image, blank=True, null=True, related_name="back_image_of")
    text_front = models.TextField(blank=True, verbose_name="Text Bildseite (Zitat)")
    text_back = models.TextField(blank=True, verbose_name="Text Adressseite (Zitat)")
    printing_method = models.ForeignKey(SkosConcept, blank=True, null=True)
    artist = models.ManyToManyField(Person, blank=True, related_name='card_creator')
    reference = models.ManyToManyField(Book, blank=True)
    published_written = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Ausgabedatum")
    published = models.DateField(blank=True, null=True)
    run_written = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="gelaufen / Datum")
    run = models.DateField(blank=True, null=True)
    hosting_institution = models.ManyToManyField(Institution, blank=True)
    note = models.TextField(blank=True, null=True, verbose_name="Formale Anmerkungen")
    note_content = models.TextField(blank=True, null=True, verbose_name="Inhaltliche Anmerkungen")
    reference = models.ManyToManyField(Book, blank=True)
    bild_motiv = models.ManyToManyField(
        SkosConcept, blank=True, related_name='bild_motiv'
    )
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
    mentioned_event = models.ManyToManyField(
        Event, blank=True, related_name='mentioned_event'
    )
    public = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.title)

    def get_next(self):
        next = Card.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Card.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def get_absolute_url(self):
        return reverse('cards:card_detail', kwargs={'pk': self.id})

    @classmethod
    def get_listview_url(self):
        return reverse('browsing:browse_cards')

    @classmethod
    def get_createview_url(self):
        return reverse('cards:card_create')
