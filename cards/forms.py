from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Card, CardCollection


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
    class Meta:
        model = Card
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)