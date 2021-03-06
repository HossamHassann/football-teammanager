"""teammanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from teams import views
from teams.views import TeamListView, GameScoreView, PlayerDetailView, TeamDetailView, AddTeamView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^teams/$', TeamListView.as_view(), name='teams-list-view'),
    url(r'^scores/$', GameScoreView.as_view(), name='game-score-view'),
    url(r'^player/(?P<slug>[-\w\x20]+)/$', PlayerDetailView.as_view(), name='player-detail-view'),
    url(r'^team/(?P<slug>[-\w\x20]+)/$', TeamDetailView.as_view(), name='team-detail-view'),
    url(r'^add_team/', AddTeamView.as_view(), name='add-team-view'),
    # url(r'^add_score/', AddScoreView.as_view(), name='add-score-view'),
]
