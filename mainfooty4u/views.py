from django.db.models import Q
from django.http import Http404
from django.contrib.auth.models import User
from django.views.generic import ListView

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Game, Matches, Leaderboard
from .serializers import GameSerializer, MatchesSerializer, LeaderboardSerializer # get from the models 

# Create your views here.

# Creating the latest games
class LatestGamesList(APIView):
    def get(self, request, format=None): # getting latest games that will showed on the front of the page 
        games = Game.objects.all()[0:4] # first 4 games 
        serializer = GameSerializer(games, many=True) # many=True as there is more than one game 
        return Response(serializer.data)

class GameDetail(APIView): # creating details of the game
    def get_object(self, matches_slug, game_slug): 
        try:
            return Game.objects.filter(matches__slug=matches_slug).get(slug=game_slug) # checking whether object exists
        except Game.DoesNotExist:
            raise Http404 # if game does not exist should alert a Http404 error from the imported library in line 2

    def get(self, request, matches_slug, game_slug, format=None): # overriding the get function
        game = self.get_object(matches_slug, game_slug) # calls the function in line 24
        serializer = GameSerializer(game) # gets all the fields from the serializer.py
        return Response(serializer.data)

class MatchesDetail(APIView): # creating details of the match
    def get_object(self, matches_slug):
        try:
            return Matches.objects.get(slug=matches_slug) # checking whether object exists
        except Game.DoesNotExist:
            raise Http404 # if game in relation to the match does not exist should alert a Http404 error from the imported library in line 2

    def get(self, request, matches_slug, format=None): # overriding the get function
        matches = self.get_object(matches_slug) # calls the function in line 36
        serializer = MatchesSerializer(matches) # gets all the fields from the serializer.py
        return Response(serializer.data)

@api_view(['POST']) # only accepts POST request to the search function
def search(request):
    query = request.data.get('query', '') # gets query from user in request data

    if query:
        games = Game.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)) # checks if name or description contains query, import Q allows advanced querysets
        serializer = GameSerializer(games, many=True) # gets all the fields from the serializer.py
        return Response(serializer.data)
    else:
        return Response({"games": []}) # if user writes empty query, it returns nothing on the page 

# 
#class LeaderboardView(generics.RetrieveAPIView):
 #   queryset = Leaderboard.objects.all()
#
 #   def get(self, request, *args, **kwargs):
  #      queryset = self.get_queryset()
   #     serializer = LeaderboardSerializer(queryset, many=True)
    #    return Response(serializer.data)
#

class LeaderboardView(ListView):
    model = Leaderboard
    template_name = 'leaderboard.html'
    context_object_name = 'leaderboard'
    ordering = ['points']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.select_related('user')
