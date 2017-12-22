from django.contrib import admin
from .models import Card, CardCollection


class CardAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'legacy_id', 'number', 'card_collection',
        'text_front', 'text_back', 'note', 'note_content'
    )
    list_filter = ['card_collection']


admin.site.register(Card, CardAdmin)
admin.site.register(CardCollection)
