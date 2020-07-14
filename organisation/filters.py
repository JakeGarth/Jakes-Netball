import django_filters
from django_filters import DateFilter, CharFilter, TimeFilter, ChoiceFilter, MultipleChoiceFilter, NumberFilter
from accounts.models import Advertisements
from teams.models import Teams
from accounts.models import Accounts
from .models import Competitions
from sports.models import Sports

from .models import *
GENDER_CHOICES = (
    ('Female', 'Female'),
    ('Male', 'Male'),
    ('Other', 'Other'),

)

COMP_GENDER_CHOICES = (
    ('Female', 'Female'),
    ('Male', 'Male'),
    ('Either', 'Either'),

)

TRUEFALSE_CHOICES = (
    ('True', 'True'),
    ('False', 'False'),

)

DAY_CHOICES = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),

)

def getSportCompTuple():
    allSports = Sports.objects.all()
    print("in getSportCompTuple")

    listOfSports = set([])
    tupleOfSports = ();
    for sport in allSports:
        listOfSports.add(sport.name)
    for sport in listOfSports:
        tupleOfSports = tupleOfSports + ((sport, sport),)
    tupleOfSports = tupleOfSports + (("", "Any"),)
    print("tup")
    print(tupleOfSports)
    return tupleOfSports




class AdvertisementsOrganisationFilter(django_filters.FilterSet):

    gender = MultipleChoiceFilter(choices = GENDER_CHOICES, label = "Gender")
    FillIn = MultipleChoiceFilter(choices = TRUEFALSE_CHOICES, label = "Fill-In")
    Permanent = MultipleChoiceFilter(choices = TRUEFALSE_CHOICES, label = "Permanent")



    class Meta:
        model = Advertisements
        fields = {
        'notes':['icontains'],
        }


class TeamsOrganisationFilter(django_filters.FilterSet):

    lookingGenderPlayers = MultipleChoiceFilter(choices=COMP_GENDER_CHOICES, label = "Gender")
    lookingNumPlayers = NumberFilter(label = "Number of vacant spots", lookup_expr='gte')
    class Meta:
        model = Teams
        fields = {
        'notes':['icontains'],

        }
        #'['sport', 'days','LatestTime','notes']
class CompetitionsOrganisationFilter(django_filters.FilterSet):

    CompetitionGender = MultipleChoiceFilter(choices = COMP_GENDER_CHOICES, label = "Gender")
    CompetitionSport = MultipleChoiceFilter(choices = getSportCompTuple, label = "Sport")
    CompetitionDay = MultipleChoiceFilter(choices = DAY_CHOICES, label = "Day")
    CompetitionGrade = django_filters.CharFilter(label='Grade', lookup_expr='icontains')

    #start_time = TimeFilter(field_name="EarliestTime", lookup_expr='gte')

    class Meta:
        model = Competitions
        fields = {

        }
