"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from api import views, form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example.urls')),
    path("easyequity",views.ee),
    path("stock-data/<id1>",views.detail),
    path("", views.jatmanis1),
    #path("filter1", views.filter1),
    #path("filter2", views.filter2)
    path("ffhe/", views.ff1),
    path("ff_admin", views.ff_admin),
    path("ffhe/player/<player_id>/", views.player),
    path("ffhe/team/<team_id>/",views.team),
    path('select-match/', form.match_selection_view, name='match_selection'),
    path('select-team/', form.team_selection_view, name='team_selection'),
    path('player-scores/', form.player_scores_view, name='player_scores'),
]
