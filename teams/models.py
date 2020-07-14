from django.db import models
from members.models import Members
from django.core.validators import MaxValueValidator, MinValueValidator


class Teams(models.Model):
    teamName = models.CharField(max_length=100, default="Jake's Team")
    day = models.CharField(max_length=100, default="Monday")
    startTimeRange = models.TimeField(auto_now=False, auto_now_add=False, default = None, null = True)
    endTimeRange = models.TimeField(auto_now=False, auto_now_add=False, default = None, null = True)
    lengthOfGame = models.CharField(max_length=100, default = "1 hour")
    location = models.CharField(max_length=100, default = "MQ Gym")
    dates = models.CharField(max_length=100, default = "Session 2")
    members = models.ManyToManyField(Members)
    sport = models.CharField(max_length=50, default = None, null = True)
    owner = models.ForeignKey('accounts.Accounts', models.CASCADE, default = None, null = True)
    notes = models.CharField(max_length=1000,  default = None, null = True)
    lookingGenderPlayers = models.CharField(max_length=10,  default = None, null = True)
    TeamCompetiton = models.ForeignKey('organisation.Competitions', models.CASCADE, default = None, null = True, blank = True)
    org = models.ForeignKey('organisation.Organisations', models.CASCADE, default = None, null = True, related_name = "OrgsofTeam")
    currentNumPlayers = models.IntegerField(default = 1, null = True, validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    lookingNumPlayers = models.IntegerField(default = 1, null = True, validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])




# Create your models here.
