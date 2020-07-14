from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from accounts.models import Accounts, Advertisements
from organisation.models import Organisations
from teams.models import Teams
from sports.models import Sports
from accounts.accountFunctions import *
import datetime
from .filters import AdvertisementsOwnFilter

login_path = "/accounts/login"
def signup_view(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             user = form.save()
             newAccount = Accounts(accountName = request.POST['username'], userInstance = user)  #This creates the Account model, has extended fields to the User model
             newAccount.save()
             login(request, user)
             return redirect('accounts:accountEdit',request.POST['username'] )
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', { 'form': form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
               return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

@login_required(login_url="/accounts/login")
def logout_view(request):
    #if request.method == 'POST':
        logout(request)
        return redirect('articles:list')

@login_required(login_url=login_path)
def account(request, accountName):
    try:
        accountInstance = Accounts.objects.get(accountName = accountName)
    except:
        return render(request, 'accounts/noAccount.html')

    accountInfo = {'name':accountName,'accountID':accountInstance.id, 'accountDescription':accountInstance.description,
    'gender':accountInstance.gender, 'accountInstance':accountInstance}
    return render(request, 'accounts/account.html', accountInfo)


@login_required(login_url=login_path)
def accountEdit(request, accountName):
    #try:
    genderList = ['Male', 'Female', 'Other']
    accountInstance = Accounts.objects.get(accountName = accountName)
    accountInfo = {'name':accountName,'accountID':accountInstance.id, 'accountDescription':accountInstance.description,
    'gender':accountInstance.gender, 'accountInstance':accountInstance,'genderList':genderList}





    #except:
        #return render(request, 'accounts/noAccount.html')
    return render(request, 'accounts/edit.html', accountInfo)

@login_required(login_url=login_path)
def accountEditMedium(request, accountName):
    if request.user.username == accountName:
    #this method is for when you are on the edit page, and this updates the database

        if request.method == 'POST':

             changingAccount = Accounts.objects.get(accountName = accountName)

             changingAccount.first_name = request.POST['First_Name']
             changingAccount.last_name = request.POST['Last_Name']
             changingAccount.phone_number = request.POST['Phone']
             changingAccount.gender = request.POST['Gender']
             changingAccount.email = request.POST['Email']
             changingAccount.description = request.POST['Description']
             changingAccount.save()


             updateAccountAds(changingAccount)
             updateAccountTeams(changingAccount)
         
    return redirect('accounts:account', accountName)


@login_required(login_url=login_path)
def accountAdvertisements(request, accountName):
    advertisementList = Advertisements.objects.filter(owner = Accounts.objects.get(accountName = accountName).id).all()
    print("sport")
    print(advertisementList[0].sport)

    myFilter = AdvertisementsOwnFilter(request.GET, queryset = advertisementList)
    advertisementList = myFilter.qs
    print("my filter")
    print(myFilter)

    return render(request, 'accounts/viewOwnAdvertisements.html', {'advertisementList':advertisementList, 'accountName':accountName, 'myFilter':myFilter})

@login_required(login_url=login_path)
def accountTeams(request, accountName):

    teamsList = Teams.objects.filter(owner = Accounts.objects.get(accountName = accountName).id).all()
    return render(request, 'accounts/viewOwnTeams.html', {'teamsList':teamsList, 'accountName':accountName})

@login_required(login_url=login_path)
def accountOrganisations(request, accountName):

    orgsList = Organisations.objects.filter(owner = Accounts.objects.get(accountName = accountName).id).all()
    return render(request, 'accounts/viewOwnOrganisations.html', {'orgsList':orgsList, 'accountName':accountName})

@login_required(login_url=login_path)
def accountOrganisationsDelete(request, accountName, orgID):

    Organisations.objects.get(id=orgID).delete()

    return redirect('accounts:accountTeams', accountName)
    return render(request, 'accounts/viewOwnOrganisations.html', {'orgsList':orgsList, 'accountName':accountName})




@login_required(login_url=login_path)
def accountOrganisationsEdit(request, accountName):

    orgsList = Organisations.objects.filter(owner = Accounts.objects.get(accountName = accountName).id).all()
    return render(request, 'accounts/viewOwnOrganisations.html', {'orgsList':orgsList, 'accountName':accountName})


@login_required(login_url=login_path)
def accountTeamsEdit(request, accountName, teamID):

    sportsList = Sports.objects.all()
    team = Teams.objects.get(id = teamID)
    startHour = converTimeToClockTime(team.startTimeRange.hour)
    startMinute = converTimeToClockTime(team.startTimeRange.minute)
    endHour = converTimeToClockTime(team.endTimeRange.hour)
    endMinute = converTimeToClockTime(team.endTimeRange.minute)
    return render(request, 'accounts/editTeam.html', {'team': team, 'sportsList':sportsList, 'accountName':accountName,
    'startHour':startHour, 'startMinute':startMinute, 'endHour':endHour, 'endMinute':endMinute,
    'listOfDaysInWeek':listOfDaysInWeek, 'listOfGenderOptions':listOfGenderOptions})

@login_required(login_url=login_path)
def accountTeamsEditMedium(request, accountName, teamID):
    if request.user.username == Teams.objects.get(id=teamID).owner.accountName:
        team = Teams.objects.get(id = teamID)

        nameOfOrg = request.POST['organisationName']
        postName = request.POST['fname']
        firstTime = request.POST['start-time'].split(':',2)
        lastTime =  request.POST['end-time'].split(':',2)
        sport =  request.POST['Sport']
        team.teamName = postName
        team.day =  request.POST['Days']
        team.location =  request.POST['teamLocation']
        team.lengthOfGame =  request.POST['lengthOfGame']
        team.startTimeRange = datetime.time(int(firstTime[0]), int(firstTime[1]), 0)
        team.endTimeRange = datetime.time(int(lastTime[0]), int(lastTime[1]), 0)
        team.owner = Accounts.objects.get(accountName = request.user.username)
        team.sport = sport
        team.currentNumPlayers = request.POST['currentPlayers']
        team.lookingNumPlayers = request.POST['lookingPlayers']
        team.lookingGenderPlayers = request.POST['genderRequirements']
        team.notes  = request.POST['Notes']
        team.save()
        print("team edited successfully")
    else:
        print("team not edited successfully")
    return redirect('accounts:accountTeams', accountName)

@login_required(login_url=login_path)
def accountTeamsDelete(request, accountName, teamID):

    team = Teams.objects.get(id = teamID)
    teamsList = Teams.objects.filter(owner = Accounts.objects.get(accountName = accountName).id).all()
    return render(request, 'accounts/deleteTeam.html', {'teamsList':teamsList, 'team':team, 'accountName':accountName})

@login_required(login_url=login_path)
def accountTeamsDeleteMedium(request, accountName, teamID):
    if request.user.username == Teams.objects.get(id=teamID).owner.accountName:
        Teams.objects.get(id=teamID).delete()
        print("Team deleted")
    else:
        print("team not deleted")
    return redirect('accounts:accountTeams', accountName)

@login_required(login_url=login_path)
def accountAdEdit(request, accountName, adID):
    ad = Advertisements.objects.get(id = adID)
    days = ad.days
    sports = ad.sport
    print('ad days')
    print(ad.days)
    print('ad sport')
    print(ad.sport)
    print(days)
    print(listOfDaysInWeek)
    sportsList = Sports.objects.all()
    startHour = converTimeToClockTime(ad.EarliestTime.hour)
    startMinute = converTimeToClockTime(ad.EarliestTime.minute)
    endHour = converTimeToClockTime(ad.LatestTime.hour)
    endMinute = converTimeToClockTime(ad.LatestTime.minute)
    return render(request, 'accounts/editAd.html', {'ad': ad,'selectedSports':sports, 'sportsList':sportsList, 'accountName':accountName,
    'startHour':startHour, 'startMinute':startMinute, 'endHour':endHour, 'endMinute':endMinute, 'days':days,'listOfDaysInWeek':listOfDaysInWeek})

@login_required(login_url=login_path)
def accountAdEditMedium(request, accountName, adID):
    if request.user.username == Advertisements.objects.get(id=adID).owner.accountName:
        print("Form in medium")
        print(request.POST)
        ad = Advertisements.objects.get(id = adID)
        notes  = request.POST['Notes']
        ad.notes = notes
        ad.save()
        print("account eddited succesfully")
    else:
        print("account did not edit succesfully")
    return redirect('accounts:accountAdvertisements', accountName)

@login_required(login_url=login_path)
def accountAdDelete(request, accountName, adID):

    ad = Advertisements.objects.get(id = adID)
    return render(request, 'accounts/deleteAd.html', {'ad':ad, 'accountName':accountName})

@login_required(login_url=login_path)
def accountAdDeleteMedium(request, accountName, adID):
    if request.user.username == Advertisements.objects.get(id=adID).owner.accountName:
        Advertisements.objects.get(id=adID).delete()
        print("ad deleted")
    else:
        print("ad not deleted")
    return redirect('accounts:accountAdvertisements', accountName)


@login_required(login_url="/accounts/login/")
def organisationDelete(request, accountName, orgID):
    org = Organisations.objects.get(id=orgID)
    return render(request, 'accounts/deleteOrganisation.html', {'org':org, 'accountName':accountName})

@login_required(login_url="/accounts/login/")
def organisationDeleteMedium(request, accountName, orgID):
    if request.user.username == Organisations.objects.get(id=orgID).owner.accountName:
        #Only creator of an org can delete it
        Organisations.objects.get(id=orgID).delete()


    try:
        return redirect('accounts:accountOrganisations', request.user.username)
    except:
        return redirect('articles:list')


@login_required(login_url=login_path)
def organisationEdit(request, accountName, orgID):
    print("we are in making org - not in medium")
    org = Organisations.objects.get(id=orgID)
    print(org)
    print(org.id)
    print(org.OrganisationName)
    # return HttpResponse('homepage')
    return render(request, 'accounts/editOrganisation.html', {'org':org})

@login_required(login_url=login_path)
def organisationEditMedium(request, accountName, orgID):
    nameOfOrg = 'test'

    if request.method == 'POST':
        try:
            oldOrg = Organisations.objects.get(id = orgID)
            if request.user.username == oldOrg.owner.accountName:
                newOrg = Organisations(id = orgID)
                print(newOrg)
                print(request.POST)
                print("here 1")
                nameOfOrg = request.POST['orgName']
                newOrg.OrganisationName = nameOfOrg
                print("here 2")
                newOrg.CompetitionRegistrationLink = request.POST['Registration_Link']
                print("here 3")
                newOrg.owner = Accounts.objects.get(accountName = accountName)
                newOrg.save()

        except Exception as e:
            print(e)
            print("Exception, not making org")
            print("It is not making an Org")
            return render(request, 'organisation/OrgMakingFail.html')

    return redirect('accounts:accountOrganisations', request.user.username)
