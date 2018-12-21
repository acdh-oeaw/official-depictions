import django_filters

from dal import autocomplete
from django import forms
from django.contrib.auth.models import User

from vocabs.models import SkosConcept
from vocabs.filters import generous_concept_filter
from entities.models import Institution, Person, Place
from . models import Card, CardCollection


class CardListFilter(django_filters.FilterSet):

    class Meta:
        model = Card
        fields = "__all__"


class CardCollectionListFilter(django_filters.FilterSet):

    class Meta:
        model = CardCollection
        fields = "__all__"