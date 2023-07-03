# Serializers allows to get information from the database and convert into Json to use on the frontend 
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Matches, Game, Leaderboard

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game # using game model from models.py 
        fields = ( # fields that will be used on the frontend 
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        )

class MatchesSerializer(serializers.ModelSerializer):
    games = GameSerializer(many=True) # gets all fields from the GameSerializer

    class Meta:
        model = Matches # using matches model from models.py
        fields = ( # fields that will be used on the frontend 
            "id",
            "name",
            "get_absolute_url",
            "games",
        )

# Leaderboard Serializer
class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        field = '__all__'

# User Serializer to make sending email work
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "email",
        )