import django_filters
from django import forms

from . models import Person, Place, Institution

DATE_LOOKUP_CHOICES = [
    ('exact', 'genaues Datum'),
    ('gte', 'später als'),
    ('lte', 'früher als'),
]


class PersonListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Person._meta.get_field('name').help_text,
        label=Person._meta.get_field('name').verbose_name
        )
    belongs_to_institution = django_filters.ModelMultipleChoiceFilter(
        queryset=Institution.objects.all(),
        help_text=Person._meta.get_field('belongs_to_institution').help_text,
        label=Person._meta.get_field('belongs_to_institution').verbose_name
        )
    place_of_birth = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.filter(is_birthplace__isnull=False).distinct(),
        help_text=Person._meta.get_field('place_of_birth').help_text,
        label=Person._meta.get_field('place_of_birth').verbose_name,
    )
    place_of_death = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.filter(is_deathplace__isnull=False).distinct(),
        help_text=Person._meta.get_field('place_of_death').help_text,
        label=Person._meta.get_field('place_of_death').verbose_name,
    )
    date_of_birth = django_filters.LookupChoiceFilter(
        field_class=forms.DateField,
        lookup_choices=DATE_LOOKUP_CHOICES,
        help_text=Person._meta.get_field('date_of_birth').help_text,
    )
    date_of_death = django_filters.LookupChoiceFilter(
        field_class=forms.DateField,
        lookup_choices=DATE_LOOKUP_CHOICES,
        help_text=Person._meta.get_field('date_of_death').help_text,
    )

    class Meta:
        model = Person
        fields = "__all__"


class PlaceListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Place._meta.get_field('name').help_text,
        label=Place._meta.get_field('name').verbose_name
        )

    class Meta:
        model = Place
        fields = "__all__"


class InstitutionListFilter(django_filters.FilterSet):
    written_name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Institution._meta.get_field('written_name').help_text,
        label=Institution._meta.get_field('written_name').verbose_name
        )

    class Meta:
        model = Institution
        fields = "__all__"
