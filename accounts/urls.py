from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.signup_view, name="signup"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    path('user/<str:accountName>', views.account, name='account'),
    path('user/<str:accountName>/edit', views.accountEdit, name='accountEdit'),
    path('user/<str:accountName>/editMedium', views.accountEditMedium, name='accountEditMedium'),


    path('user/<str:accountName>/organisations', views.accountOrganisations, name='accountOrganisations'),
    path('user/<str:accountName>/teams', views.accountTeams, name='accountTeams'),
    path('user/<str:accountName>/advertisements', views.accountAdvertisements, name='accountAdvertisements'),

    path('user/<str:accountName>/<str:orgID>/deleteOrganisation', views.organisationDelete, name='organisationDelete'),
    path('user/<str:accountName>/<str:orgID>/deleteOrganisation/medium', views.organisationDeleteMedium, name='organisationDeleteMedium'),
    path('user/<str:accountName>/<str:orgID>/editOrganisation', views.organisationEdit, name='organisationEdit'),
    path('user/<str:accountName>/<str:orgID>/editOrganisation/medium', views.organisationEditMedium, name='organisationEditMedium'),


    path('user/<str:accountName>/<str:teamID>/editTeam', views.accountTeamsEdit, name='accountTeamsEdit'),
    path('user/<str:accountName>/<str:teamID>/editTeam/medium', views.accountTeamsEditMedium, name='accountTeamsEditMedium'),
    path('user/<str:accountName>/<str:teamID>/deleteTeam', views.accountTeamsDelete, name='accountTeamsDelete'),
    path('user/<str:accountName>/<str:teamID>/deleteTeam/medium', views.accountTeamsDeleteMedium, name='accountTeamsDeleteMedium'),

    path('user/<str:accountName>/<str:adID>/editAd', views.accountAdEdit, name='accountAdEdit'),
    path('user/<str:accountName>/<str:adID>/editAd/medium', views.accountAdEditMedium, name='accountAdEditMedium'),
    path('user/<str:accountName>/<str:adID>/deleteAd', views.accountAdDelete, name='accountAdDelete'),
    path('user/<str:accountName>/<str:adID>/deleteAd/medium', views.accountAdDeleteMedium, name='accountAdDeleteMedium'),

]
