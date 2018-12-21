from django import forms
from dal import autocomplete
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div, MultiField, HTML
from crispy_forms.bootstrap import *

from .models import Card, CardCollection

from entities.models import Institution
from vocabs.models import SkosConcept


class CardCollectionFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(CardCollectionFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Accordion(
                AccordionGroup(
                    'Basic search options',
                    'name',
                    'abbreviation',
                    css_id="basic_search_fields"
                    ),
                )
            )


class CardCollectionForm(forms.ModelForm):

    class Meta:
        model = CardCollection
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CardCollectionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class CardForm(forms.ModelForm):
    archiv = forms.ModelChoiceField(
        required=False,
        queryset=Institution.objects.filter(institution_type="Archiv")
    )

    class Meta:
        model = Card
        fields = "__all__"
        widgets = {
            'subject_norm': autocomplete.ModelSelect2Multiple(
                url='/vocabs-ac/specific-concept-ac/schlagwort'),
            'creator_inst': autocomplete.ModelSelect2Multiple(
                url='entities-ac:institution-autocomplete'),
            'creator_person': autocomplete.ModelSelect2Multiple(
                url='entities-ac:person-autocomplete'),
            'mentioned_inst': autocomplete.ModelSelect2Multiple(
                url='entities-ac:institution-autocomplete'),
            'mentioned_person': autocomplete.ModelSelect2Multiple(
                url='entities-ac:person-autocomplete'),
            'mentioned_place': autocomplete.ModelSelect2Multiple(
                url='entities-ac:place-autocomplete'),
            'rel_res': autocomplete.ModelSelect2Multiple(
                url='archiv-ac:archresource-autocomplete'),
        }

    def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class GenericFilterFormHelper(FormHelper):

    def __init__(self, *args, **kwargs):
        super(GenericFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))


class CardFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(CardFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Accordion(
                AccordionGroup(
                    'Basic search options',
                    'title',
                    'res_type',
                    css_id="basic_search_fields"
                    ),
                AccordionGroup(
                    'Inhalt',
                    'subject_norm',
                    'abstract',
                    css_id="more"
                    ),
                AccordionGroup(
                    'Datierung',
                    'written_date',
                    'not_before',
                    'not_after',
                    css_id="datierung"
                    ),
                AccordionGroup(
                    'Bestand',
                    'archiv',
                    'signature',
                    css_id="bestand"
                    ),
                AccordionGroup(
                    'Personen',
                    'creator_person',
                    'mentioned_person',
                    css_id="personen"
                    ),
                AccordionGroup(
                    'Institutionen',
                    'creator_inst',
                    'mentioned_inst',
                    css_id="institutionen"
                    ),
                AccordionGroup(
                    'Orte',
                    'mentioned_place',
                    css_id="orte"
                    ),
                AccordionGroup(
                    'Verantwortlich',
                    'creators',
                    css_id="Verantwortlich"
                    ),
                )
            )
