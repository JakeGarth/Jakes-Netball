from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from teams import views
urlpatterns = [

    #url('', views.displayTeams, name="displayTeams"),
    url('joining', views.joiningTeams, name="joiningTeams"),
    url('maketeam', views.makingTeams, name="makingTeams"),
]
