import django_tables2 as tables
from django_tables2.config import RequestConfig
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView

from browsing.browsing_utils import GenericListView, BaseCreateView, BaseUpdateView

from vocabs.models import SkosConceptScheme, SkosConcept
from . filters import *
from . forms import *
from . tables import *
from . models import Card


class CardListView(GenericListView):
    model = Card
    filter_class = CardListFilter
    formhelper_class = CardFilterFormHelper
    table_class = CardTable
    init_columns = [
        'id',
        'title',
        'signature',
    ]


class CardDetailView(DetailView):
    model = Card
    template_name = 'card/card_detail.html'


class CardCreate(BaseCreateView):

    model = Card
    form_class = CardForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CardCreate, self).dispatch(*args, **kwargs)


class CardUpdate(BaseUpdateView):

    model = Card
    form_class = CardForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CardUpdate, self).dispatch(*args, **kwargs)


class CardDelete(DeleteView):
    model = Card
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('card:card_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CardDelete, self).dispatch(*args, **kwargs)
