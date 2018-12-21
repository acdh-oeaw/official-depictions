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

    @classmethod
    def get_listview_url(self):
        return reverse('cards:cardcollection_browse')

    @classmethod
    def get_createview_url(self):
        return reverse('cards:cardcollection_create')

    def get_absolute_url(self):
        return reverse('cards:cardcollection_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('cards:cardcollection_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('cards:cardcollection_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'card:cardcollection_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'card:cardcollection_detail',
                kwargs={'pk': prev.first().id}
            )
        return False


class Card(IdProvider):
    """This class describes a post-card like entity"""
    legacy_id = models.IntegerField(blank=True, null=True, verbose_name="Lfd. Nr.")
    sort_id = models.IntegerField(blank=True, null=True, verbose_name="Chronologie")
    number = models.CharField(max_length=25, blank=True, verbose_name="Nr (Serie)")
    card_collection = models.ForeignKey(
        CardCollection, blank=True, null=True, verbose_name="Serie",
        related_name="contain_cards", on_delete=models.SET_NULL
    )
    text_front = models.TextField(blank=True, verbose_name="Text Bildseite (Zitat)")
    img_front = models.CharField(
        blank=True, verbose_name="Vorderseite", max_length=250
    )
    text_back = models.TextField(blank=True, verbose_name="Text Rückseite")
    img_back = models.CharField(
        blank=True, verbose_name="Rückseite", max_length=250
    )
    note = models.TextField(
        blank=True, null=True, verbose_name="Formale Anmerkungen"
    )
    note_content = models.TextField(
        blank=True, null=True, verbose_name="Inhaltliche Anmerkungen"
    )
    archiv = models.ForeignKey(
        Institution, null=True, blank=True,
        verbose_name="Archiv",
        help_text="Archiv in dem das Dokument aufbewahrt wird",
        related_name="has_docs_archived",
        on_delete=models.SET_NULL
    )
    signature = models.TextField(
        blank=True, verbose_name="(Archiv)Signatur",
        help_text="(Archiv)Signatur"
    )
    written_date = models.CharField(
        max_length=250, blank=True, verbose_name="Datum original",
        help_text="Datum original"
    )
    not_before = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True,
        verbose_name="Nicht vor normalisiert",
        help_text="YYYY-MM-DD"
    )
    not_after = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True,
        verbose_name="Nicht nach normalisiert",
        help_text="YYYY-MM-DD"
    )
    subject_norm = models.ManyToManyField(
        SkosConcept, blank=True,
        help_text="Schlagwörter normalisiert",
        verbose_name="Schlagwörter normalisiert",
        related_name="subject_norm_of"
    )
    creator_person = models.ManyToManyField(
        Person, blank=True,
        help_text="Erzeuger des Dokuments",
        verbose_name="Erzeuger des Dokuments(Person)",
        related_name="created_by_person"
    )
    creator_inst = models.ManyToManyField(
        Institution, blank=True,
        help_text="Erzeuger des Dokuments(Institution)",
        verbose_name="Erzeuger des Dokuments(Institution)",
        related_name="created_by_inst"
    )
    mentioned_person = models.ManyToManyField(
        Person, blank=True,
        help_text="Im Dokument erwähnte Person",
        verbose_name="Im Dokument erwähnte Person",
        related_name="pers_mentioned_in_res"
    )
    mentioned_inst = models.ManyToManyField(
        Institution, blank=True,
        help_text="Im Dokument erwähnte Institution",
        verbose_name="Im Dokument erwähnte Institution",
        related_name="inst_mentioned_in_res"
    )
    mentioned_place = models.ManyToManyField(
        Place, blank=True,
        help_text="Im Dokument erwähnte Orte",
        verbose_name="Im Dokument erwähnte Orte",
        related_name="place_mentioned_in_res"
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
