from django.contrib import admin
from .models import Institution, Person, Event
from .models_base import NormDataRecord

admin.site.register(Institution)
admin.site.register(Person)
admin.site.register(Event)
admin.site.register(NormDataRecord)

# Register your models here.
