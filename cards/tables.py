import django_tables2 as tables
from django_tables2.utils import A
from entities.models import *
from . models import *


class CardCollectionTable(tables.Table):
    id = tables.LinkColumn(verbose_name='ID')

    class Meta:
        model = CardCollection
        sequence = ('id', )
        attrs = {"class": "table table-responsive table-hover"}


class CardTable(tables.Table):
    id = tables.LinkColumn(verbose_name='ID')

    class Meta:
        model = Card
        sequence = ('id', )
        attrs = {"class": "table table-responsive table-hover"}
