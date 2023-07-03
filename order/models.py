from django.contrib.auth.models import User
from django.db import models

from mainfooty4u.models import Game
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE) # connects user to the model via foreign key
    first_name = models.CharField(max_length=100) # first name of user making order
    last_name = models.CharField(max_length=100) # last name of user making order
    email = models.CharField(max_length=100) # email of user
    address = models.CharField(max_length=100) # address of user
    postcode = models.CharField(max_length=100) # postcode of user
    place = models.CharField(max_length=100) # place of user
    phone = models.CharField(max_length=100) # phone of user
    created_at = models.DateTimeField(auto_now_add=True) # when creating a new order on the backend it will automatically fill a date time to know when it has been added to the database 
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True) # paid amount by user, decimal_places=2 as Great British Pounds is set to two decimal places
    stripe_token = models.CharField(max_length=100) # saves stripe token 

    class Meta:
        ordering = ['-created_at',] # descending order in my account page

    def __str__(self):
        return self.first_name 

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE) # reference to order via foreign key
    game = models.ForeignKey(Game, related_name='items', on_delete=models.CASCADE) #  reference to game via foreign key
    price = models.DecimalField(max_digits=8, decimal_places=2) # price of the order
    quantity = models.IntegerField(default=1) # quantity, default = 1 

    def __str__(self):
        return '%s' % self.id # id easy to see in database