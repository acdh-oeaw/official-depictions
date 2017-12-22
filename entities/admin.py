from django.contrib import admin
from .models import Place, AlternativeName, Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('written_name', 'name', 'forename')


admin.site.register(Person, PersonAdmin)
admin.site.register(AlternativeName)
