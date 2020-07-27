from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation

from django.conf import settings
from handle.models import Pid
from entities.models import Person, Institution, Place
from idprovider.models import IdProvider
from vocabs.models import SkosConcept

IIIF_SERVER = settings.APIS_IIIF_SERVER


class CardCollection(IdProvider):
    """ Describebes a series of cards """

    name = models.CharField(
        max_length=250, blank=True,
        verbose_name="Name der Sammlung"
    )
    abbreviation = models.CharField(
        max_length=25, blank=True,
        verbose_name="Sammlungskürzel"
    )
    description = models.TextField(
        blank=True, verbose_name="Beschreibung"
    )
    part_of = models.ForeignKey(
        'CardCollection',
        blank=True, null=True, verbose_name="Teilsammlung von",
        related_name="has_parts",
        help_text="Ist Teilsammlung von",
        on_delete=models.SET_NULL
    )

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
                'cards:cardcollection_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'cards:cardcollection_detail',
                kwargs={'pk': prev.first().id}
            )
        return False


class Card(IdProvider):
    """This class describes a post-card like entity"""
    legacy_id = models.IntegerField(
        blank=True, null=True, verbose_name="Lfd. Nr.",
        help_text="""Laufende Nummer. Alle identifizierten Karten, inklusive der Variationen, wurden mit fortlaufenden Nummern versehen. Auch für unidentifizierte Karten wurde eine laufende Nummer vergeben, und zwar einerseits für fehlende Nummern der Hauptserie und andererseits wenn ergänzende Quellen (Presseberichte, Verkaufslisten, Archivquellen etc.) einen bestimmten Kartentitel nennen, aufgrund derer diese Karten künftig identifiziert und zugeordnet werden könnten (vgl. z. B. die Thomas-Riss-Karten Nr. 959-967)."""
    )
    sort_id = models.IntegerField(
        blank=True, null=True, verbose_name="Chronologie"
    )
    number = models.CharField(
        max_length=25, blank=True, verbose_name="Nr (Serie)"
    )
    card_collection = models.ForeignKey(
        CardCollection, blank=True, null=True, verbose_name="Serie",
        related_name="contain_cards",
        help_text="Zur besseren Zuordnung wurden die Karten einer chronologischen und formalen Serie zugeordnet.",
        on_delete=models.SET_NULL
    )
    text_front = models.TextField(
        blank=True, verbose_name="Text Bildseite (Zitat)",
        help_text="Alle Textelemente der Bildseite wurden hier buchstabengetreu eingetragen. Auf den Karten visuell getrennte Textelemente wurden durch ein Semikolon getrennt. Die Reihung beginnt immer mit der Widmung und erfolgt dann üblicherweise gegen den Uhrzeigersinn."
    )
    img_front = models.CharField(
        blank=True, verbose_name="Bildseite", max_length=250
    )
    text_back = models.TextField(
        blank=True, verbose_name="Text Adressseite",
        help_text="Alle Textelemente der Adressseite wurden hier buchstabengetreu eingetragen. Auf den Karten visuell getrennte Textelemente wurden durch ein Semikolon getrennt. Die Reihung beginnt immer mit der Widmung und erfolgt dann üblicherweise gegen den Uhrzeigersinn"
    )
    img_back = models.CharField(
        blank=True, verbose_name="Adressseite", max_length=250
    )
    gelaufen = models.CharField(
        max_length=250, blank=True, verbose_name="gelaufen",
        help_text="Bezeichnet, ob die Karte postalisch versandt wurde (gel. für gelaufen) oder nicht (n. gel. für nicht gelaufen)."
    )
    note = models.TextField(
        blank=True, null=True, verbose_name="Formale Anmerkungen"
    )
    note_content = models.TextField(
        blank=True, null=True, verbose_name="Inhaltliche Anmerkungen"
    )
    archiv = models.ForeignKey(
        Institution, null=True, blank=True,
        verbose_name="Archiv/Quelle",
        help_text="Quelle, anhand derer die Texte von Bild- und Adressseite in die Datenbank eingetragen wurden.",
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
    bild_technik = models.ManyToManyField(
        SkosConcept, blank=True,
        help_text="Bildtechnik",
        verbose_name="Bildtechnik",
        related_name="bildtechnik_of"
    )
    subject_norm = models.ManyToManyField(
        SkosConcept, blank=True,
        help_text="Schlagwörter normalisiert",
        verbose_name="Schlagwörter normalisiert",
        related_name="subject_norm_of"
    )
    creator_person = models.ManyToManyField(
        Person, blank=True,
        verbose_name="Erzeuger des Bildes (Person)",
        related_name="created_by_person",
        help_text="Der Name des Künstlers bzw. Illustrators ist in der standardisierten Form Nachname, Vorname(n) angegeben. Dies umfasst lediglich den Künstler des Bildes, nicht jedoch Verfasser abgedruckter Gedichte oder Lieder.",
    )
    creator_inst = models.ManyToManyField(
        Institution, blank=True,
        help_text="Erzeuger des Bildes (Institution)",
        verbose_name="Erzeuger des Bildes (Institution)",
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
    pid = GenericRelation(Pid, blank=True, null=True, related_query_name="get_pid")

    def __str__(self):
        if self.signature:
            return "{}".format(self.signature)
        else:
            return "{}".format(self.id)

    @classmethod
    def get_listview_url(self):
        return reverse('cards:card_browse')

    @classmethod
    def get_createview_url(self):
        return reverse('cards:card_create')

    def get_arche_url(self):
        return reverse('cards:card_arche', kwargs={'pk': self.id})

    def get_absolute_url(self):
        return reverse('cards:card_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('cards:card_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('cards:card_edit', kwargs={'pk': self.id})

    def get_tei_url(self):
        return reverse('cards:card_as_tei', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'cards:card_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_thumb_front(self):
        if self.img_front:
            thumb_url = f"{IIIF_SERVER}/{self.img_front}/full/250,/0/default.jpg"
        else:
            thumb_url = None
        return thumb_url

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'cards:card_detail',
                kwargs={'pk': prev.first().id}
            )
        return False
