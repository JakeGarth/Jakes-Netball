from django.shortcuts import render, redirect
from teams.models import Teams
from members.models import Members
from organisation.models import Organisations
from django.contrib.auth.decorators import login_required
from accounts.models import Accounts, Advertisements
from sports.models import Sports
import datetime
from .filters import AdvertisementsOrganisationFilter, TeamsOrganisationFilter, CompetitionsOrganisationFilter
from .models import Organisations, Competitions
from accounts.accountFunctions import listOfGenderOptions
from accounts.accountFunctions import *

# Create your views here.

login_path = "/accounts/login"
@login_required(login_url=login_path)
def organisationHome(request, nameOfOrg):
    print("nameOfOrg")
    print(nameOfOrg)
    org = Organisations.objects.get(OrganisationName = nameOfOrg)
    return render(request, 'organisation/organisationHome.html',{'orgName':nameOfOrg, 'org':org})

@login_required(login_url=login_path)
def makeOrg(request):
    print("we are in making org - not in medium")
    # return HttpResponse('homepage')
    return render(request, 'organisation/makeOrganisation.html')

@login_required(login_url=login_path)
def makeOrgMedium(request):
    nameOfOrg = 'test'
    if request.method == 'POST':
        try:
            nameOfOrg = request.POST['orgName']
            CompetitionRegistrationLink = request.POST['Registration_Link']
            newORG = Organisations(OrganisationName = nameOfOrg, owner = Accounts.objects.get(accountName = request.user.username),
            CompetitionRegistrationLink = CompetitionRegistrationLink)
            newORG.save()
        except:
            print("Exception, not making org")
            print("It is not making an Org")
            return render(request, 'organisation/OrgMakingFail.html')
    return redirect('organisation:organisationHome', nameOfOrg)

    # return HttpResponse('homepage')

@login_required(login_url=login_path)
def makeOrgFail(request):
    print("do we get in makeOrgFail")
    nameOfOrg = '.'
    return render(request, 'organisation/OrgMakingFail.html', nameOfOrg)

@login_required(login_url=login_path)
def addTeam(request, nameOfOrg):
    print("we are in add Team")
    if request.method == 'POST':
        print("THIS IS A POST:")
        print(request.POST)
        nameOfOrg = request.POST['organisationName']
    sportsList = Sports.objects.all()
    print(nameOfOrg)
    # return HttpResponse('homepage')
    return render(request, 'organisation/addTeam.html', {'nameOfOrg':nameOfOrg, 'sportsList':sportsList})

@login_required(login_url=login_path)
def addTeamMedium(request, nameOfOrg):
    print("WE ARE IN THE MEDIUMMMM")
    if request.method == 'POST':
        print("we are in joining teams")
        try:
            print("Checking if adding team:")
            print(request.POST)
            nameOfOrg = request.POST['organisationName']
            postName = request.POST['fname']
            print(postName)
            print("team day")
            print(request.POST['Days'])
            firstTime = request.POST['start-time'].split(':',2)
            lastTime =  request.POST['end-time'].split(':',2)
            sport =  request.POST['Sport']

            team = Teams(teamName = postName, day =  request.POST['Days'], location =  request.POST['teamLocation'],
            lengthOfGame =  request.POST['lengthOfGame'], startTimeRange = datetime.time(int(firstTime[0]), int(firstTime[1]), 0),
            endTimeRange = datetime.time(int(lastTime[0]), int(lastTime[1]), 0), owner = Accounts.objects.get(accountName = request.user.username)
            , sport = sport, currentNumPlayers = request.POST['currentPlayers'], lookingNumPlayers = request.POST['lookingPlayers'],
            lookingGenderPlayers = request.POST['genderRequirements'], notes  = request.POST['Notes'], org = Organisations.objects.get(OrganisationName = nameOfOrg))
            team.save()

            print("team id")
            print(team.id)
            print("nameOfOrg: ")
            print(nameOfOrg)
            print("before org")
            org = Organisations.objects.get(OrganisationName=nameOfOrg)
            print("after org")
            org.teams.add(team)
        except Exception as e:
            print(e)
            print("not adding a team - something went wrong?")
    # return HttpResponse('homepage')
    return redirect('organisation:organisationHome', nameOfOrg, {'org':org})


@login_required(login_url=login_path)
def addTeamComp(request, nameOfOrg, compID):
    print("we are in add Team")
    if request.method == 'POST':
        print("THIS IS A POST:")
        print(request.POST)
        nameOfOrg = request.POST['organisationName']
    sportsList = Sports.objects.all()
    print(nameOfOrg)
    # return HttpResponse('homepage')
    return render(request, 'organisation/addTeamCompetition.html', {'nameOfOrg':nameOfOrg, 'sportsList':sportsList, 'compID':compID})

@login_required(login_url=login_path)
def addTeamCompMedium(request, nameOfOrg, compID):
    print("WE ARE IN THE MEDIUMMMM")
    if request.method == 'POST':
        print("we are in joining teams for a comp")
        try:
            comp = Competitions.objects.get(id = compID)
            sport = comp.CompetitionSport
            day = comp.CompetitionDay
            location = comp.CompetitionLocation
            length = comp.LengthOfGame
            startTime = comp.CompetitionStartTime
            endTime = comp.CompetitionEndTime

            print("Checking if adding team:")
            print(request.POST)
            nameOfOrg = request.POST['organisationName']
            postName = request.POST['fname']

            team = Teams(teamName = postName, day = day, location = location, lengthOfGame =  length, startTimeRange = startTime,
            endTimeRange = endTime, owner = Accounts.objects.get(accountName = request.user.username), sport = sport,
            currentNumPlayers = request.POST['currentPlayers'], lookingNumPlayers = request.POST['lookingPlayers'],
            lookingGenderPlayers = request.POST['genderRequirements'], notes  = request.POST['Notes'], org = Organisations.objects.get(OrganisationName = nameOfOrg),
            TeamCompetiton = comp)
            team.save()

            org = Organisations.objects.get(OrganisationName=nameOfOrg)
            org.teams.add(team)
        except Exception as e:
            print(e)
            print("not adding a team - something went wrong?")
    # return HttpResponse('homepage')
    return redirect('organisation:organisationHome', nameOfOrg)

@login_required(login_url=login_path)
def addAdvertisement(request, nameOfOrg):
    # return HttpResponse('homepage')
    sportsList = Sports.objects.all()
    print(sportsList)
    return render(request, 'organisation/addAdvertisement.html', {'nameOfOrg':nameOfOrg, 'sportsList':sportsList})

@login_required(login_url=login_path)
def addAdvertisementComp(request, nameOfOrg, compID):
    # return HttpResponse('homepage')
    sportsList = Sports.objects.all()
    print(sportsList)
    return render(request, 'organisation/addAdvertisementComp.html', {'nameOfOrg':nameOfOrg, 'sportsList':sportsList, 'compID':compID})

@login_required(login_url=login_path)
def addAdvertisementCompMedium(request, nameOfOrg, compID):
    #this method saves the advertisement information in the database
    print("In advertisement medium comp")
    print(request.POST)
    comp = Competitions.objects.get(id = compID)

    sport = comp.CompetitionSport
    days = comp.CompetitionDay
    earlyTime = comp.CompetitionStartTime
    lateTime = comp.CompetitionEndTime
    notes = request.POST['Notes']
    owner = Accounts.objects.get(accountName = request.user.username)
    gender = owner.gender
    ownerFirstName = owner.first_name
    ownerLastName = owner.last_name

    org = Organisations.objects.get(OrganisationName=nameOfOrg)
    try:
        FillIn = request.POST['FillIn']
    except:
        FillIn = False

    try:
        Permanent = request.POST['permanent']
    except:
        Permanent = False

    print("Fill in")
    print(FillIn)
    print(" permanent ")
    print(Permanent)

    advertisement = Advertisements(org = org, EarliestTime = earlyTime, LatestTime = lateTime,sport = sport, days = days, gender = gender,
    owner = owner, notes = notes, AdvertisementCompetiton = comp, FillIn = FillIn, Permanent = Permanent, ownerFirstName = ownerFirstName, ownerLastName = ownerLastName)

    advertisement.save()
    # return HttpResponse('homepage')
    return redirect('organisation:organisationHome', nameOfOrg)

@login_required(login_url=login_path)
def addAdvertisementMedium(request, nameOfOrg):
    #this method saves the advertisement information in the database
    print("In advertisement medium")
    print(request.POST)
    try:
        daysList = request.POST.getlist('Days')
    except:
        daysList = []
    try:
        sportsList = request.POST.getlist('Sport')
    except:
        sportsList = []


    firstTime = request.POST['start-time'].split(':',2)
    earlyTime = datetime.time(int(firstTime[0]), int(firstTime[1]), 0)
    endTime = request.POST['end-time'].split(':',2)
    lateTime = datetime.time(int(endTime[0]), int(endTime[1]), 0)

    notes = request.POST['Notes']
    owner = Accounts.objects.get(accountName = request.user.username)
    gender = owner.gender
    org = Organisations.objects.get(OrganisationName=nameOfOrg)



    advertisement = Advertisements(org = org, EarliestTime = earlyTime, LatestTime = lateTime,sport = sportsList, days = daysList, gender = gender, owner = owner, notes = notes)

    advertisement.save()
    # return HttpResponse('homepage')
    return redirect('organisation:organisationHome', nameOfOrg, {'org':org})

@login_required(login_url=login_path)
def viewAdvertisements(request, nameOfOrg):
    # delete this view
    advertisementList = Advertisements.objects.filter(org = Organisations.objects.get(OrganisationName=nameOfOrg).id)

    print(Accounts.objects.get(accountName = request.user.username))
    account = Accounts.objects.get(accountName = request.user.username)
    myFilter = AdvertisementsOrganisationFilter(request.GET, queryset = advertisementList)
    advertisementList = myFilter.qs
    return render(request, 'organisation/viewAdvertisements.html', {'nameOfOrg':nameOfOrg, 'advertisementList': advertisementList, 'account':account, 'myFilter':myFilter})

@login_required(login_url=login_path)
def viewCompetitionAdvertisements(request, nameOfOrg, compID):
    advertisementList = Advertisements.objects.filter(org = Organisations.objects.get(OrganisationName=nameOfOrg).id, AdvertisementCompetiton = compID)

    account = Accounts.objects.get(accountName = request.user.username)
    filter = AdvertisementsOrganisationFilter(request.GET, queryset = advertisementList)

    advertisementList = filter.qs
    org = Organisations.objects.get(OrganisationName = nameOfOrg)
    return render(request, 'organisation/viewAdvertisements.html', {'nameOfOrg':nameOfOrg, 'advertisementList': advertisementList, 'account':account, 'filter':filter, 'org':org})

@login_required(login_url=login_path)
def viewTeams(request, nameOfOrg):
    teamsList = Teams.objects.filter(org = Organisations.objects.get(OrganisationName=nameOfOrg).id)

    account = Accounts.objects.get(accountName = request.user.username)
    return render(request, 'organisation/viewTeams.html', {'nameOfOrg':nameOfOrg, 'teamsList':teamsList, 'account':account})

@login_required(login_url=login_path)
def viewCompetitionTeams(request, nameOfOrg, compID):
    #displays table of teams of a corresponding competition
    print(nameOfOrg)
    print(compID)
    comp = Competitions.objects.get(id = compID)
    account = Accounts.objects.get(accountName = request.user.username)
    teamsList = Teams.objects.filter(org = Organisations.objects.get(OrganisationName=nameOfOrg).id, TeamCompetiton = compID)
    #teamsList = Teams.objects.filter(org = Organisations.objects.get(OrganisationName=nameOfOrg).id, TeamCompetiton = comp)
    org = Organisations.objects.get(OrganisationName = nameOfOrg)
    filter = TeamsOrganisationFilter(request.GET, queryset = teamsList)
    print("filter")
    print(filter)
    teamsList = filter.qs
    return render(request, 'organisation/viewCompetitionTeams.html', {'nameOfOrg':nameOfOrg, 'account':account, 'teamsList':teamsList, 'org':org, 'filter':filter})

@login_required(login_url=login_path)
def viewCompetitions(request, nameOfOrg):
    account = Accounts.objects.get(accountName = request.user.username)
    compList = Competitions.objects.filter(CompetitionOrganisation = Organisations.objects.get(OrganisationName = nameOfOrg))
    filter = CompetitionsOrganisationFilter(request.GET, queryset = compList)
    compList = filter.qs
    org = Organisations.objects.get(OrganisationName = nameOfOrg)
    return render(request, 'organisation/viewCompetitions.html', {'nameOfOrg':nameOfOrg, 'account':account, 'compList':compList, 'org':org, 'filter':filter})

@login_required(login_url=login_path)
def addCompetitions(request, nameOfOrg):
    # return HttpResponse('homepage')
    sportsList = Sports.objects.all()
    try:
        org = Organisations.objects.get(OrganisationName=nameOfOrg)
        orgOwner = org.owner.accountName
    except:
         orgOwner = "."

    genderList = listOfGenderOptions
    print(genderList)
    return render(request, 'organisation/addCompetition.html', {'nameOfOrg':nameOfOrg, 'orgOwner':orgOwner, 'sportsList':sportsList, 'genderList':genderList})

@login_required(login_url=login_path)
def addCompetitionsMedium(request, nameOfOrg):
    print("in add competition medium")

    print("lol")
    print(request.POST)
    CompetitionDay = request.POST['Days']
    CompetitionSport = request.POST['Sport']
    CompetitionLocation = request.POST['Location']
    CompetitionGrade = request.POST['Grade']
    CompetitionGender = request.POST['Gender']
    CompetitionStartTime = request.POST['start-time']
    CompetitionEndTime = request.POST['end-time']
    CompetitionStartDate = request.POST['start-date']

    print(CompetitionStartDate)
    CompetitionEndDate = request.POST['end-date']
    LengthOfGame = request.POST['length']
    org = Organisations.objects.get(OrganisationName = nameOfOrg)
    owner = Accounts.objects.get(accountName = request.user.username)
    print("issue is declaring")
    comp = Competitions(CompetitionDay = CompetitionDay, CompetitionSport = CompetitionSport, CompetitionLocation = CompetitionLocation,  owner = owner,
     CompetitionGrade = CompetitionGrade, CompetitionGender = CompetitionGender, CompetitionOrganisation = org, CompetitionEndTime = CompetitionEndTime,
     CompetitionStartTime = CompetitionStartTime, LengthOfGame = LengthOfGame,CompetitionStartDate = CompetitionStartDate,
     CompetitionEndDate = CompetitionEndDate)

    comp.save()

    return redirect('organisation:organisationHome', nameOfOrg)

@login_required(login_url=login_path)
def competitionDelete(request, compID):
    print("In deleting comp")
    comp = Competitions.objects.get(id = compID)
    return render(request, 'organisation/deleteCompetition.html', {'comp':comp})

@login_required(login_url=login_path)
def competitionDeleteMedium(request, compID):
    if request.user.username == Competitions.objects.get(id=compID).CompetitionOrganisation.owner.accountName:
        #Only creator of comp can delete a comp
        orgNameOfComp = Competitions.objects.get(id=compID).CompetitionOrganisation.OrganisationName
        Competitions.objects.get(id=compID).delete()

    try:
        return redirect('organisation:organisationHome', orgNameOfComp)
    except:
        return redirect('articles:list')




@login_required(login_url=login_path)
def joiningTeamMedium(request, nameOfOrg):
    try:
        firstNamee = request.POST['firstName']
        lastNamee = request.POST['lastName']
        member = Members(firstName = firstNamee, lastName = lastNamee)
        member.save()
        team = Teams.objects.get(id=request.POST['teamID'])
        team.members.add(member)
        org = Organisations.objects.get(OrganisationName = nameOfOrg)
    except:
        print("it is not a member")
    return redirect('organisation:organisationHome', nameOfOrg, {'org':org})

@login_required(login_url=login_path)
def makeSport(request):
    # return HttpResponse('homepage')
    sportsList = Sports.objects.all()
    print(sportsList)
    print("You are in make sport")
    return render(request, 'organisation/makeSport.html')

@login_required(login_url=login_path)
def makeSportMedium(request):
    print("You are in medium")
    newSport = Sports(name = request.POST['fname'])
    newSport.save()
    return redirect('home')


@login_required(login_url=login_path)
def editCompetition(request, compID):
    # return HttpResponse('homepage')

    comp = Competitions.objects.get(id = compID)

    org = Competitions.objects.get(id = compID).CompetitionOrganisation
    if request.user.username == org.owner.accountName:
        nameOfOrg = org.OrganisationName
        orgOwner = org.owner.accountName
        genderList = listOfGenderOptions
        print(genderList)
        sportsList = Sports.objects.all()
        print("here")
        startTimeValue = converTimeToClockTime(comp.CompetitionStartTime.hour)+":"+converTimeToClockTime(comp.CompetitionStartTime.minute)
        endTimeValue = converTimeToClockTime(comp.CompetitionEndTime.hour)+":"+converTimeToClockTime(comp.CompetitionEndTime.minute)



        return render(request, 'organisation/editCompetition.html', {'org':org, 'orgOwner':orgOwner, 'sportsList':sportsList, 'genderList':genderList, 'listOfDaysInWeek':listOfDaysInWeek, 'comp':comp,
        'startTimeValue':startTimeValue, 'endTimeValue':endTimeValue})
    else:
        return redirect('organisation:organisationHome', org.OrganisationName)

@login_required(login_url=login_path)
def editCompetitionMedium(request, compID):
    previousComp = Competitions.objects.get(id=compID)
    org = previousComp.CompetitionOrganisation
    if request.user.username == org.owner.accountName:
        print("in edit competition medium")
        print(compID)
        previousComp = Competitions.objects.get(id=compID)
        org = previousComp.CompetitionOrganisation
        print("lol")
        print(request.POST)
        CompetitionDay = request.POST['Days']
        CompetitionSport = request.POST['Sport']
        CompetitionLocation = request.POST['Location']
        CompetitionGrade = request.POST['Grade']
        CompetitionGender = request.POST['Gender']
        CompetitionStartTime = request.POST['start-time']
        CompetitionEndTime = request.POST['end-time']
        CompetitionStartDate = request.POST['start-date']
        CompetitionEndDate = request.POST['end-date']
        LengthOfGame = request.POST['length']
        org = Organisations.objects.get(id = previousComp.CompetitionOrganisation.id)
        owner = Accounts.objects.get(accountName = request.user.username)
        print("issue is declaring")
        comp = Competitions(id = compID, CompetitionDay = CompetitionDay, CompetitionSport = CompetitionSport, CompetitionLocation = CompetitionLocation,  owner = owner,
         CompetitionGrade = CompetitionGrade, CompetitionGender = CompetitionGender, CompetitionOrganisation = org, CompetitionEndTime = CompetitionEndTime,
         CompetitionStartTime = CompetitionStartTime, LengthOfGame = LengthOfGame,CompetitionStartDate = CompetitionStartDate,
         CompetitionEndDate = CompetitionEndDate)
        comp.save()

    return redirect('organisation:organisationHome', org.OrganisationName)


@login_required(login_url=login_path)
def testHTML(request):
    print("we are in test HTML")
    # return HttpResponse('homepage')
    return render(request, 'organisation/testHTML.html')
