from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cards/detail/(?P<pk>[0-9]+)$', views.CardDetailView.as_view(),
        name='card_detail'),
    url(r'^cards/create/$', views.CardCreate.as_view(),
        name='card_create'),
    url(r'^cards/edit/(?P<pk>[0-9]+)$', views.CardUpdate.as_view(),
        name='card_edit'),
    url(r'^cards/delete/(?P<pk>[0-9]+)$', views.CardDelete.as_view(),
        name='card_delete'),
]
