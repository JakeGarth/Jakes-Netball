from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from organisation import views
from django.urls import path

app_name = 'Sports'
urlpatterns = [
    #url('', views.displayTeams, name="displayTeams")
    url('makesport', views.makeSport, name="makeSport"),
]
