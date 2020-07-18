from django.http import HttpResponse

from django.shortcuts import get_object_or_404

from . models import Card
from . tei_utils import card_to_tei


def as_tei(request, pk):
    card_object = get_object_or_404(Card, pk=pk)
    mytei = card_to_tei(card_object)
    return HttpResponse(mytei, content_type="text/xml")
