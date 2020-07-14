from accounts.models import Accounts, Advertisements
from organisation.models import Organisations
from teams.models import Teams
from sports.models import Sports
import datetime

listOfDaysInWeek = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
listOfGenderOptions = ['Female', 'Male', 'Either']

def converTimeToClockTime(time):

    if time < 10:
        stringHour = "0"+str(time)
    else:
        stringHour = str(time)
    print("stringHour: "+stringHour)
    return stringHour

def updateAccountAds(account):
    print("in update accounts ads")
    accountAds = Advertisements.objects.filter(owner = account)
    if len(accountAds) > 0:
        for ad in accountAds:
            print("in for loop")
            print(account.first_name)
            print(account.last_name)
            ad.ownerFirstName = account.first_name
            ad.ownerLastName = account.last_name
            ad.gender = account.gender
            ad.save()

def updateAccountTeams(account):
    accountTeams = Teams.objects.filter(owner = account)
    print("in update accounts teams")
