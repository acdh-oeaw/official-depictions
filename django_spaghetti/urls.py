from django.conf.urls import url
from django_spaghetti.views import plate

app_name = 'django_spaghetti'

urlpatterns = [
    url(r'^$', plate, name='plate'),
]
