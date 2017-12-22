from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from .forms import CardForm, CardCollectionForm
from .models import Card, CardCollection


class CardCollectionDetailView(DetailView):
    model = CardCollection
    template_name = 'cards/cardcol_detail.html'


class CardCollectionCreate(CreateView):

    model = CardCollection
    form_class = CardCollectionForm
    template_name = 'cards/cardcol_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CardCollectionCreate, self).dispatch(*args, **kwargs)


class CardCollectionUpdate(UpdateView):

    model = CardCollection
    form_class = CardCollectionForm
    template_name = 'cards/cardcol_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CardCollectionUpdate, self).dispatch(*args, **kwargs)


class CardCollectionDelete(DeleteView):
    model = CardCollection
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_cards')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CardCollectionDelete, self).dispatch(*args, **kwargs)


class CardDetailView(DetailView):
    model = Card
    template_name = 'cards/card_detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CardDetailView, self).dispatch(*args, **kwargs)


class CardCreate(CreateView):

    model = Card
    form_class = CardForm
    template_name = 'cards/card_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CardCreate, self).dispatch(*args, **kwargs)


class CardUpdate(UpdateView):

    model = Card
    form_class = CardForm
    template_name = 'cards/card_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CardUpdate, self).dispatch(*args, **kwargs)


class CardDelete(DeleteView):
    model = Card
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('browsing:browse_cards')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CardDelete, self).dispatch(*args, **kwargs)
