from django.conf.urls import url
from . import views

app_name = 'cards'

urlpatterns = [
    url(
        r'^card/$',
        views.CardListView.as_view(),
        name='card_browse'
    ),
    url(
        r'^card/detail/(?P<pk>[0-9]+)$',
        views.CardDetailView.as_view(),
        name='card_detail'
    ),
    url(
        r'^card/create/$',
        views.CardCreate.as_view(),
        name='card_create'
    ),
    url(
        r'^card/edit/(?P<pk>[0-9]+)$',
        views.CardUpdate.as_view(),
        name='card_edit'
    ),
    url(
        r'^card/delete/(?P<pk>[0-9]+)$',
        views.CardDelete.as_view(),
        name='card_delete'),
]
