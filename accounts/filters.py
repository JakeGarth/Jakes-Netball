import django_filters
from django_filters import DateFilter, CharFilter, TimeFilter, ChoiceFilter

from .models import *
STATUS_CHOICES = (
    ('Female', 'Female'),
    ('Male', 'Male'),
    ('Either', 'Either'),
)
class AdvertisementsOwnFilter(django_filters.FilterSet):

    gender = ChoiceFilter(choices=STATUS_CHOICES)

    class Meta:
        model = Advertisements
        fields = {
        'sport':['icontains'],
        'days':['icontains'],
        'LatestTime':['icontains'],
        'notes':['icontains'],

        }
    
