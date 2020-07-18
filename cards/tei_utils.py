import datetime
import lxml.etree as ET

from django.conf import settings

from django.template.loader import get_template


def card_to_tei(card_object):
    template = get_template('cards/card_tei.xml')
    context = {'object': card_object}
    temp_str = f"{template.render(context=context)}"
    node = ET.fromstring(temp_str)
    xml = ET.tostring(node, pretty_print=True, encoding='UTF-8')
    return xml
