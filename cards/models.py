from django.db import models
from django.urls import reverse

from entities.models import Person, Institution, Place
from images.models import Image
from idprovider.models import IdProvider
from vocabs.models import SkosConcept


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

    # def get_absolute_url(self):
    #     return reverse('cardss:cardcol_detail', kwargs={'pk': self.id})
    #
    # @classmethod
    # def get_listview_url(self):
    #     return reverse('browsing:browse_cardcollections')
    #
    # @classmethod
    # def get_createview_url(self):
    #     return reverse('cardss:cardcol_create')


class Card(IdProvider):
    """This class describes a post-card like entity"""
    legacy_id = models.IntegerField(blank=True, null=True, verbose_name="Lfd. Nr.")
    sort_id = models.IntegerField(blank=True, null=True, verbose_name="Chronologie")
    number = models.CharField(max_length=25, blank=True, verbose_name="Nr (Serie)")
    card_collection = models.ForeignKey(
        CardCollection, blank=True, null=True, verbose_name="Serienkürzel",
        related_name="contain_cards", on_delete=models.SET_NULL
    )
    text_front = models.TextField(blank=True, verbose_name="Text Bildseite (Zitat)")
    text_back = models.TextField(blank=True, verbose_name="Text Adressseite (Zitat)")
    artist = models.ManyToManyField(
        Person, blank=True, related_name='card_creator', verbose_name="Künstler"
    )
    note = models.TextField(
        blank=True, null=True, verbose_name="Formale Anmerkungen"
    )
    note_content = models.TextField(
        blank=True, null=True, verbose_name="Inhaltliche Anmerkungen"
    )
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
    scan_front = models.ForeignKey(
        Image, blank=True, null=True, related_name="front_image_of", on_delete=models.SET_NULL,
        verbose_name="Vorderseite"
    )
    scan_back = models.ForeignKey(
        Image, blank=True, null=True,
        related_name="back_image_of", on_delete=models.SET_NULL,
        verbose_name="Rückseite"
    )
    public = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.id)

    @classmethod
    def get_listview_url(self):
        return reverse('cards:card_browse')

    @classmethod
    def get_createview_url(self):
        return reverse('cards:card_create')

    def get_absolute_url(self):
        return reverse('cards:card_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('cards:card_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('cards:card_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'card:card_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'card:card_detail',
                kwargs={'pk': prev.first().id}
            )
        return False
