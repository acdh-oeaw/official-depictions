import os
from django.db import models
from django.conf import settings
from django.urls import reverse
from idprovider.models import IdProvider


try:
    base_url = settings.IIIF_BASE
except:
    base_url = "https://iiif.acdh.oeaw.ac.at/"

IIIF_PATH = "{}".format(base_url)
FILE_EXTENSION_CHOICES = (
    ('.tif', 'tif'),
    ('.jpg', '.jpg'),
    ('.jp2', '.jp2'),
)


def set_directory_path(instance, filename):
    if instance.directory:
        return '{0}/{1}'.format(instance.directory, filename)
    else:
        return filename


class ServerPath(IdProvider):
    name = models.CharField(default=IIIF_PATH, blank=True, max_length=250)

    def __str__(self):
        return "{}".format(self.name)


class Image(IdProvider):
    path = models.ForeignKey(ServerPath, blank=True, null=True, on_delete=True)
    directory = models.CharField(blank=True, max_length=250)
    custom_filename = models.CharField(blank=True, max_length=250)
    file_extension = models.CharField(
        blank=True, max_length=20, choices=FILE_EXTENSION_CHOICES, default='.jp2')
    upload = models.FileField(upload_to=set_directory_path, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.path is None:
            temp_path, _ = ServerPath.objects.get_or_create(name=IIIF_PATH)
            self.path = temp_path
        else:
            pass
        if self.upload:
            self.custom_filename = self.upload.name

        super(Image, self).save(*args, **kwargs)

    def get_next(self):
        next = Image.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Image.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    @property
    def full_path(self):
        if self.directory == "":
            path = "{}/{}/info.json".format(self.path, self.custom_filename)
        else:
            path = "{}{}/{}/info.json".format(self.path, self.directory, self.custom_filename)
        path = path.replace('.jp2', '')
        return path

    @property
    def iiif_endpoint(self):
        if self.directory == "":
            path = "{}/{}".format(self.path, self.custom_filename)
        else:
            path = "{}{}/{}".format(self.path, self.directory, self.custom_filename)
        path = path.replace('.jp2', '')
        return path

    @property
    def fetch_binary(self):
        return "{}/full/full/0/default.jpg".format(self.iiif_endpoint)

    def __str__(self):
        return self.full_path

    def get_absolute_url(self):
        return reverse('images:image_detail', kwargs={'pk': self.id})

    @classmethod
    def get_listview_url(self):
        return reverse('images:image_list')
