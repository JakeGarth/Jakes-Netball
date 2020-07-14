from django.http import HttpResponse
from django.shortcuts import render


def joiningTeams(request):
    if request.method == 'POST':
        print("POST")
        print(request)
        print(request.POST)
        try:
            postTeamName = request.POST['teamName']
            teamID = request.POST['teamID']
            orgName =  request.POST['orgName']
        except:
            print("nothing")
    print("we are in joining teams")
    print("Post team name: "+postTeamName)
    print("Post team ID: "+ teamID)
    # return HttpResponse('homepage')
    return render(request, 'teams/joiningTeam.html', {'postTeamName':postTeamName, 'orgName':orgName, 'teamID':request.POST['teamID']})


def makingTeams(request):
    print("we are in joining teams")
    print("in this one")
    # return HttpResponse('homepage')
    return render(request, 'teams/makingTeam.html')
