from django.conf.urls import url
from . import views
from . import tei_views
from archeutils import views as arche_views


app_name = 'cards'

urlpatterns = [
    url(
        r'^ids$',
        arche_views.get_ids,
        name='get_ids'
    ),
    url(
        r'^arche$',
        arche_views.project_as_arche_graph,
        name='project_as_arche'
    ),
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
        r'^card/tei/(?P<pk>[0-9]+)$',
        tei_views.as_tei,
        name='card_as_tei'
    ),
    url(
        r'^card/arche/(?P<pk>[0-9]+)$',
        arche_views.res_as_arche_graph,
        name='card_arche'
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
    url(
        r'^cardcollection/$',
        views.CardCollectionListView.as_view(),
        name='cardcollection_browse'
    ),
    url(
        r'^cardcollection/detail/(?P<pk>[0-9]+)$',
        views.CardCollectionDetailView.as_view(),
        name='cardcollection_detail'
    ),
    url(
        r'^cardcollection/create/$',
        views.CardCollectionCreate.as_view(),
        name='cardcollection_create'
    ),
    url(
        r'^cardcollection/edit/(?P<pk>[0-9]+)$',
        views.CardCollectionUpdate.as_view(),
        name='cardcollection_edit'
    ),
    url(
        r'^cardcollection/delete/(?P<pk>[0-9]+)$',
        views.CardCollectionDelete.as_view(),
        name='cardcollection_delete'),
]
