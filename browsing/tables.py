import django_tables2 as tables
from django_tables2.utils import A
from entities.models import *
from cards.models import Card, CardCollection


class CardCollectionTable(tables.Table):
    name = tables.Column()
    abbreviation = tables.LinkColumn(
        'cards:cardcol_detail',
        args=[A('pk')], verbose_name='Name'
    )
    card_collection = tables.Column()

    class Meta:
        model = CardCollection
        sequence = ('name', 'abbreviation')
        attrs = {"class": "table table-responsive table-hover"}


class CardTable(tables.Table):
    legacy_id = tables.Column()
    number = tables.Column()
    title = tables.LinkColumn(
        'cards:card_detail',
        args=[A('pk')], verbose_name='Name'
    )
    card_collection = tables.Column()

    class Meta:
        model = Card
        sequence = ('legacy_id', 'number', 'title', 'card_collection')
        attrs = {"class": "table table-responsive table-hover"}


class PersonTable(tables.Table):
    id = tables.LinkColumn(
        'entities:person_detail',
        args=[A('pk')], verbose_name='ID'
    )
    name = tables.LinkColumn(
        'entities:person_detail',
        args=[A('pk')], verbose_name='Name'
    )
    forename = tables.Column()

    class Meta:
        model = Person
        sequence = ('id', 'written_name',)
        attrs = {"class": "table table-responsive table-hover"}


class InstitutionTable(tables.Table):
    written_name = tables.LinkColumn(
        'entities:institution_detail',
        args=[A('pk')], verbose_name='Name'
    )
    location = tables.Column()

    class Meta:
        model = Institution
        sequence = ('id', 'written_name',)
        attrs = {"class": "table table-responsive table-hover"}


class PlaceTable(tables.Table):
    name = tables.LinkColumn(
        'entities:place_detail',
        args=[A('pk')], verbose_name='Name'
    )
    part_of = tables.Column()

    class Meta:
        model = Place
        sequence = ('id', 'name',)
        attrs = {"class": "table table-responsive table-hover"}


class AlternativeNameTable(tables.Table):
    name = tables.LinkColumn(
        'entities:alternativename_detail',
        args=[A('pk')], verbose_name='Name'
    )

    class Meta:
        model = AlternativeName
        sequence = ('name',)
        attrs = {"class": "table table-responsive table-hover"}
