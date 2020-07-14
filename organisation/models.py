from django.db import models
from teams.models import Teams
from datetime import datetime

GENDER_CHOICES = (
    ('Male','Male'),
    ('Female', 'Female'),
    ('Either','Either'),
)

class Organisations(models.Model):
    OrganisationName = models.CharField(max_length=30, default= None, unique = True)
    teams = models.ManyToManyField(Teams)
    owner = models.ForeignKey('accounts.Accounts', models.CASCADE, default = None, null = True)
    CompetitionRegistrationLink = models.CharField(max_length=100, default= None, blank = True, null = True)


class Competitions(models.Model):
    CompetitionDay = models.CharField(max_length=10, default= None, blank = True)
    CompetitionSport = models.CharField(max_length=25, default= None, blank = True)
    CompetitionGender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Either', blank = True)
    CompetitionLocation = models.CharField(max_length=100, default = None, blank = True)
    CompetitionGrade = models.CharField(max_length=10, default = None, blank = True)
    LengthOfGame = models.CharField(max_length=100, default = None, blank = True)
    CompetitionStartTime = models.TimeField(auto_now=False, auto_now_add=False, default = None, null = True, blank = True)
    CompetitionEndTime = models.TimeField(auto_now=False, auto_now_add=False, default = None, null = True, blank = True)
    CompetitionStartDate = models.DateField(default=None, blank=True)
    CompetitionEndDate = models.DateField(default=None, blank=True)
    owner = models.ForeignKey('accounts.Accounts', models.CASCADE, default = None, null = True, blank = True)
    CompetitionOrganisation = models.ForeignKey('Organisations', models.CASCADE, default = None, null = True, blank = True)



# Create your models here.
