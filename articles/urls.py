from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'articles'

urlpatterns = [
    
    url(r'^$', views.article_list, name="list"),
    path('allteams', views.allTeams, name="allTeams"),
    url(r'^create/$', views.article_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),

]
