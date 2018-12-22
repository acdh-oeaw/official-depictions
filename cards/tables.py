import django_tables2 as tables
from django_tables2.utils import A
from entities.models import *
from . models import *


class CardCollectionTable(tables.Table):
    id = tables.LinkColumn(verbose_name='ID')
    abbreviation = tables.LinkColumn(verbose_name='Abk.')

    class Meta:
        model = CardCollection
        sequence = ('id', )
        attrs = {"class": "table table-responsive table-hover"}


class CardTable(tables.Table):
    signature = tables.LinkColumn()
    legacy_id = tables.LinkColumn(
        verbose_name='Lfd. Nr.'
    )
    mentioned_person = tables.ManyToManyColumn()
    mentioned_inst = tables.ManyToManyColumn()
    mentioned_place = tables.ManyToManyColumn()
    creator_person = tables.ManyToManyColumn()
    creator_inst = tables.ManyToManyColumn()
    subject_norm = tables.ManyToManyColumn()
    bild_technik = tables.ManyToManyColumn()

    class Meta:
        model = Card
        sequence = ('legacy_id', 'signature', 'card_collection',)
        attrs = {"class": "table table-responsive table-hover"}
