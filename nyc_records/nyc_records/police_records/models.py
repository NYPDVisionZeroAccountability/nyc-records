from django.db import models
from django.forms import ModelForm
# from django.contrib.auth.models import User


RECORD_TYPE_CHOICES = (
    ('MOV', 'Moving Violation'),
    ('CMP', 'Compstat'),
)

BOROUGH_CHOICES = (
    ('MN', 'Manhattan'),
    ('BK', 'Brooklyn'),
    ('BX', 'Bronx'),
    ('QN', 'Queens'),
    ('SI', 'Staten Island'),
)

SOURCE_CHOICES = (
    ('TRAL', 'Transportation Alternatives'),
    ('NYPD', 'New York Police Department'),
)

class Precinct(models.Model):
    precinct = models.TextField(max_length=255, default='')
    precinct_id = models.BooleanField(default=False)
    borough = models.CharField(max_length=2, choices=BOROUGH_CHOICES)


class Record(models.Model):
    '''
        Information to store about the record 
    '''
    date = models.DateField()
    source = models.CharField(max_length=4, choices=RECORD_TYPE_CHOICES)
    url = models.CharField(max_length=255, choices=RECORD_TYPE_CHOICES)
    record_type = models.CharField(max_length=3, choices=RECORD_TYPE_CHOICES)
    precinct = models.ForeignKey(Precinct, null=True,
                                 default=None, blank=True)

class MovingViolation(models.Model):
    record = models.ForeignKey(Record, null=True,
                               default=None, blank=True)
    violation = models.CharField(max_length=255)

class Compstat(models.Model):
    record = models.ForeignKey(Record, null=True,
                               default=None, blank=True)
    offense = models.CharField(max_length=255)