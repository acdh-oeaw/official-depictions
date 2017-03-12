import re
import unicodedata
from datetime import datetime
from django.db import models
from .validators import date_validator


def match_date(date):
    """Function to parse string-dates into python date objects.
    """
    date = date.strip()
    date = date.replace('-', '.')
    if re.match(r'[0-9]{4}$', date):
        dr = datetime.strptime(date, '%Y')
        dr2 = date
    elif re.match(r'[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{4}$', date):
        dr = datetime.strptime(date, '%d.%m.%Y')
        dr2 = date
    elif re.match(r'[0-9]{4}\.\.\.$', date):
        dr = datetime.strptime(date, '%Y...')
        dr2 = re.match(r'([0-9]{4})\.\.\.$', date).group(1)
    elif re.match(r'[0-9]{4}\.[0-9]{1,2}\.\.$', date):
        dr = datetime.strptime(date, '%Y.%m..')
        dr2 = re.match(r'([0-9]{4})\.([0-9]{1,2})\.\.$', date).group(2)
        +'.'+re.match(r'([0-9]{4})\.([0-9]{1,2})\.\.$', date).group(1)
    elif re.match(r'[0-9]{4}\.[0-9]{1,2}\.[0-9]{1,2}$', date):
        dr = datetime.strptime(date, '%Y.%m.%d')
        dr3 = re.match(r'([0-9]{4})\.([0-9]{1,2})\.([0-9]{1,2})$', date)
        dr2 = dr3.group(3)+'.'+dr3.group(2)+'.'+dr3.group(1)
    else:
        dr = None
        dr2 = dr2 = date
    return dr, dr2


class NormDataRecord(models.Model):
    url = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.url


class TempEntityClass(models.Model):
    """ Base class to bind common attributes to many classes.

    The common attributes are:
    written start and enddates
    recognized start and enddates which are derived by RegEx
    from the written dates.
    A review boolean field to mark an object as reviewed
    """
    name = models.CharField(max_length=255, blank=True)
    review = models.BooleanField(
        default=False,
        help_text="Should be set to True, if the data record holds up quality standards.")
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    start_date_written = models.CharField(
        max_length=255, blank=True, null=True,
        validators=[date_validator, ], verbose_name="Start",
        help_text="Please enter a date (DD).(MM).YYYY")
    end_date_written = models.CharField(
        max_length=255, blank=True, null=True,
        validators=[date_validator, ], verbose_name="End",
        help_text="Please enter a date (DD).(MM).YYYY")
    note = models.TextField(blank=True, null=True)
    norm_data_reference = models.ManyToManyField(NormDataRecord, blank=True)

    def __str__(self):
        if self.name != "":  # relation usually don´t have names

            return self.name
        else:
            return "(ID: {})".format(self.id)

    def save(self, *args, **kwargs):
        """Adaption of the save() method of the class to automatically parse string-dates into date objects
        """
        if self.start_date_written:
            self.start_date, self.start_date_written = match_date(self.start_date_written)
        if self.end_date_written:
            self.end_date, self.end_date_written = match_date(self.end_date_written)
        if self.name:
            self.name = unicodedata.normalize('NFC', self.name)
        super(TempEntityClass, self).save(*args, **kwargs)
        return self

    class Meta:
        abstract = True
