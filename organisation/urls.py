from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from organisation import views
from django.urls import path

app_name = 'organisation'
urlpatterns = [
    #url('', views.displayTeams, name="displayTeams"),

    path('maketeam/<str:nameOfOrg>', views.addTeam, name='addTeam'),
    path('maketeamcompetition/<str:nameOfOrg>/<str:compID>', views.addTeamComp, name='addTeamComp'),
    path('maketeamcompetition/medium/<str:nameOfOrg>/<str:compID>', views.addTeamCompMedium, name='addTeamCompMedium'),
    path('viewteams/<str:nameOfOrg>', views.viewTeams, name='viewTeams'),
    path('maketeam/medium/<str:nameOfOrg>', views.addTeamMedium, name='addTeamMedium'),
    path('jointeam/medium/<str:nameOfOrg>', views.joiningTeamMedium, name='joiningTeamMedium'),

    path('viewCompetitions/<str:nameOfOrg>', views.viewCompetitions, name='viewCompetitions'),
    path('competitionDelete/<str:compID>', views.competitionDelete, name='competitionDelete'),
    path('competitionDelete/medium/<str:compID>', views.competitionDeleteMedium, name='competitionDeleteMedium'),
    path('competitionEdit/<str:compID>', views.editCompetition, name='editCompetition'),
    path('competitionEdit/medium/<str:compID>', views.editCompetitionMedium, name='editCompetitionMedium'),

    path('competition/teamview/<str:nameOfOrg>/<str:compID>', views.viewCompetitionTeams, name='viewCompetitionTeams'),
    path('addCompetitions/<str:nameOfOrg>', views.addCompetitions, name='addCompetitions'),
    path('addCompetitions/medium/<str:nameOfOrg>', views.addCompetitionsMedium, name='addCompetitionsMedium'),

    path('makeadvertisement/<str:nameOfOrg>', views.addAdvertisement, name='addAdvertisement'),
    path('makeadvertisementcompetition/<str:nameOfOrg>/<str:compID>', views.addAdvertisementComp, name='addAdvertisementComp'),
    path('makeadvertisementcompetition/medium/<str:nameOfOrg>/<str:compID>', views.addAdvertisementCompMedium, name='addAdvertisementCompMedium'),
    path('viewadvertisements/<str:nameOfOrg>', views.viewAdvertisements, name='viewAdvertisements'),
    path('viewadvertisementscompetition/<str:nameOfOrg>/<str:compID>', views.viewCompetitionAdvertisements, name='viewCompetitionAdvertisements'),
    path('makeadvertisement/medium/<str:nameOfOrg>', views.addAdvertisementMedium, name='addAdvertisementMedium'),



    path('makeorganisation/medium', views.makeOrgMedium, name='makeOrgMedium'),
    url('makeorganisation/fail', views.makeOrgFail, name="makeOrgFail"),
    url('makeorganisation', views.makeOrg, name="makeOrg"),
    path('home/<str:nameOfOrg>', views.organisationHome, name='organisationHome'),




    url('makeSportMedium', views.makeSportMedium, name="makeSportMedium"),
    url('makeSport', views.makeSport, name="makeSport"),

    url('testHTML', views.testHTML, name="testHTML"),

]
