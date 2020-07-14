from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms
from teams.models import Teams
from members.models import Members
from organisation.models import Organisations

@login_required(login_url="/accounts/login")
def article_list(request):
    print(request)
    if request.method == 'POST':
        print("THIS IS A POST:")
        print(request.POST)
        try:
            postName = request.POST['fname']
            print(postName)
            team = Teams(teamName = postName, day =  request.POST['teamDay'] , location =  request.POST['teamLocation'],
            lengthOfGame =  request.POST['lengthOfGame'], startTimeRange =  request.POST['startTime'])
            team.save()
        except:
            print("It is not a team")


    try:
        print("look here")
        print(relatedTeam.members.all())
    except:
        print("print didnt work")

    teamsList = Teams.objects.all()
    orgList = Organisations.objects.all()


    articles = Article.objects.all().order_by('date');
    return render(request, 'articles/article_list.html', { 'articles': articles, 'teamsList' : teamsList, 'orgList':orgList})

@login_required(login_url="/accounts/login")
def allTeams(request):
    print(request)
    if request.method == 'POST':
        print("THIS IS A POST:")
        print(request.POST)
        try:
            postName = request.POST['fname']
            print(postName)
            team = Teams(teamName = postName, day =  request.POST['teamDay'] , location =  request.POST['teamLocation'],
            lengthOfGame =  request.POST['lengthOfGame'], startTimeRange =  request.POST['startTime'])
            team.save()
        except:
            print("It is not a team")

#looking here till line 40

        try:

            firstNamee = request.POST['firstName']
            print(firstNamee)
            lastNamee = request.POST['lastName']
            print(lastNamee)
            print('test')
            member = Members(firstName = firstNamee, lastName = lastNamee)
            print("create member")

            member.save()
            print("member saved")
            print("post team name: ")
            print(request.POST)
            team = Teams.objects.get(teamName=request.POST['postTeamName'])
            team.members.add(member)
            print("Do we get to the end?")
            print(team.members)
        except:
            print("it is not a member")

    print("testing")
    #print(request.POST['postTeamName'])
    #relatedTeam = Teams.objects.get(teamName=request.POST['postTeamName'])

    try:
        print("look here")
        print(relatedTeam.members.all())
    except:
        print("print didnt work")

    teamsList = Teams.objects.all()
    orgList = Organisations.objects.all()

    print(teamsList)
    for object in teamsList:
        print(object.teamName)
    print("ids")

    print(Teams.objects.filter(id='1'))

    articles = Article.objects.all().order_by('date');
    return render(request, 'articles/allTeams.html', { 'articles': articles, 'teamsList' : teamsList, 'orgList':orgList})

@login_required(login_url="/accounts/login")
def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', { 'article': article })

def testing(request, slug):

    return render(request, 'articles/testing.html')

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', { 'form': form })
