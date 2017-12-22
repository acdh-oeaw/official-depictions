import django_filters
from dal import autocomplete
from entities.models import Place, AlternativeName, Institution, Person
from cards.models import CardCollection, Card

django_filters.filters.LOOKUP_TYPES = [
    ('', '---------'),
    ('exact', 'Is equal to'),
    ('iexact', 'Is equal to (case insensitive)'),
    ('not_exact', 'Is not equal to'),
    ('lt', 'Lesser than/before'),
    ('gt', 'Greater than/after'),
    ('gte', 'Greater than or equal to'),
    ('lte', 'Lesser than or equal to'),
    ('startswith', 'Starts with'),
    ('endswith', 'Ends with'),
    ('contains', 'Contains'),
    ('icontains', 'Contains (case insensitive)'),
    ('not_contains', 'Does not contain'),
]


class CardCollectionListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=CardCollection._meta.get_field('name').help_text,
        label=CardCollection._meta.get_field('name').verbose_name
        )
    abbreviation = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=CardCollection._meta.get_field('abbreviation').help_text,
        label=CardCollection._meta.get_field('abbreviation').verbose_name
        )

    class Meta:
        model = CardCollection
        fields = "__all__"


class CardListFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Card._meta.get_field('title').help_text,
        label=Card._meta.get_field('title').verbose_name
        )
    text_front = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Card._meta.get_field('text_front').help_text,
        label=Card._meta.get_field('text_front').verbose_name
        )
    text_back = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Card._meta.get_field('text_back').help_text,
        label=Card._meta.get_field('text_back').verbose_name
        )
    card_collection = django_filters.ModelMultipleChoiceFilter(
        queryset=CardCollection.objects.all(),
        help_text=Card._meta.get_field('card_collection').help_text,
        label=Card._meta.get_field('card_collection').verbose_name
        )
    artist = django_filters.ModelMultipleChoiceFilter(
        queryset=Person.objects.all(),
        help_text=Card._meta.get_field('artist').help_text,
        label=Card._meta.get_field('artist').verbose_name
        )

    class Meta:
        model = Card
        fields = "__all__"


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

    class Meta:
        model = Person
        fields = "__all__"


class InstitutionListFilter(django_filters.FilterSet):
    written_name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Institution._meta.get_field('written_name').help_text,
        label=Institution._meta.get_field('written_name').verbose_name
        )
    alt_names = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Institution._meta.get_field('alt_names').help_text,
        label=Institution._meta.get_field('alt_names').verbose_name
        )
    authority_url = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Institution._meta.get_field('authority_url').help_text,
        label=Institution._meta.get_field('authority_url').verbose_name
        )
    location = django_filters.ModelMultipleChoiceFilter(
        queryset=AlternativeName.objects.all(),
        help_text=Institution._meta.get_field('location').help_text,
        label=Institution._meta.get_field('location').verbose_name
        )

    class Meta:
        model = Institution
        fields = [
            'id', 'written_name', 'authority_url', 'location'
        ]


class PlaceListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Place._meta.get_field('name').help_text,
        label=Place._meta.get_field('name').verbose_name
        )
    geonames_id = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=Place._meta.get_field('geonames_id').help_text,
        label=Place._meta.get_field('geonames_id').verbose_name
        )
    alternative_name = django_filters.ModelMultipleChoiceFilter(
        queryset=AlternativeName.objects.all(),
        help_text=Place._meta.get_field('alternative_name').help_text,
        label=Place._meta.get_field('alternative_name').verbose_name
        )
    part_of = django_filters.ModelMultipleChoiceFilter(
        queryset=Place.objects.all(),
        help_text=Place._meta.get_field('part_of').help_text,
        label=Place._meta.get_field('part_of').verbose_name
        )

    class Meta:
        model = Place
        fields = [
            'id'
        ]


class AlternativeNameListFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        help_text=AlternativeName._meta.get_field('name').help_text,
        label=AlternativeName._meta.get_field('name').verbose_name
        )

    class Meta:
        model = AlternativeName
        fields = [
            'id'
        ]
