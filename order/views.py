import stripe # talks to stripe api

from django.conf import settings # gets secret key
from django.contrib.auth.models import User # to get user
from django.http import Http404 # for checking errors
from django.shortcuts import render 

# libraries needed from rest framework
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, OrderItem
from .serializers import OrderSerializer, MyOrderSerializer

@api_view(['POST']) # only post require
@authentication_classes([authentication.TokenAuthentication]) # makes sure user is authenticated
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data) # gets data from the form in checkout page
 
    if serializer.is_valid(): # all data is correct, we can proceed to checkout
        stripe.api_key = settings.STRIPE_SECRET_KEY # from settings file
        paid_amount = sum(item.get('quantity') * item.get('game').price for item in serializer.validated_data['items']) # calculates the paid amount for every item in the serializer


        try: # if payment is not successful we must show error to user
            charge = stripe.Charge.create(
                amount=int(paid_amount * 100), # stripe wants this in cents
                currency='GBP', # set to GBP
                description='Charge from Footy4U', 
                source=serializer.validated_data['stripe_token'] # stripe token from frontend
            )

            serializer.save(user=request.user, paid_amount=paid_amount)

            return Response(serializer.data, status=status.HTTP_201_CREATED) # frontend knows everything is ok code (201)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # show error 404 bad request if there is something wrong with serializer

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None): # overriding the get function
        orders = Order.objects.filter(user=request.user) # only want order from the authenticated user
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)