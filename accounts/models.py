from django.db import models
from django.contrib.auth.models import User
from organisation.models import Organisations
from teams.models import Teams
from sports.models import Sports
import datetime
from django_mysql.models import ListCharField
# Create your models here.

class Accounts(models.Model):
    accountName = models.CharField(max_length=100, default="NoNameMade", unique=True)
    organisationsMade = models.ManyToManyField(Organisations, related_name = "AccountOrgsMade")
    organisationsJoined = models.ManyToManyField(Organisations, related_name = "AccountOrgsJoined")
    teamsJoined = models.ManyToManyField(Teams, related_name = "AccountTeamsJoined")
    teamsMade = models.ManyToManyField(Teams, related_name = "AccountTeamsMade")
    userInstance = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    email = models.EmailField(max_length=50, blank=True)
    first_name = models.CharField(max_length=50, default="Anon")
    last_name = models.CharField(max_length=50, default="Smith")
    phone_number = models.CharField(max_length=15, blank=True)
    description = models.CharField(max_length=1000, default="Hey! I love playing netball!")
    gender = models.CharField(max_length=10, default = "Female")
    image = models.ImageField(default='sharon.png', blank=True)

class Advertisements(models.Model):
    sport = models.CharField(max_length=25, default= None, blank = True)
    days = models.CharField(max_length=10, default= None, blank = True)
    EarliestTime = models.TimeField(auto_now=False, auto_now_add=False, default = None, null = True)
    LatestTime = models.TimeField(auto_now=False, auto_now_add=False, default = None, null = True)
    gender = models.CharField(max_length=10, default = "Female")
    owner = models.ForeignKey('accounts.Accounts', models.CASCADE, default = None, null = True)
    ownerFirstName = models.CharField(max_length=50, default="Anon")
    ownerLastName = models.CharField(max_length=50, default="Smith")
    notes = models.CharField(max_length=1000, default = "")
    org = models.ForeignKey('organisation.Organisations', models.CASCADE, default = None, null = True)
    fakeColumn = models.CharField(max_length=1000, default = "", null = True)
    AdvertisementCompetiton = models.ForeignKey('organisation.Competitions', models.CASCADE, default = None, null = True, blank = True)
    FillIn = models.BooleanField(default=False)
    Permanent = models.BooleanField(default=False)




     #cascade means if user is deleted, account is deleted, and vice versa
