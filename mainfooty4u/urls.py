# seperate urls file to keep code tidy
from django.urls import path, include

from mainfooty4u import views

from .views import LeaderboardView

urlpatterns = [
    path('latest-games/', views.LatestGamesList.as_view()), # shows all of the latest games 
    path('games/search/', views.search), # shows available games based on user search
    path('games/<slug:matches_slug>/<slug:game_slug>/', views.GameDetail.as_view()), # renders the game details as a view to show the games
    path('games/<slug:matches_slug>/', views.MatchesDetail.as_view()), # shows all types of games based on matches being 5 a side/7 a side
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
]