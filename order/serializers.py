from rest_framework import serializers

from .models import Order, OrderItem

from mainfooty4u.serializers import GameSerializer # get game serializer as it is connected to the orders

class MyOrderItemSerializer(serializers.ModelSerializer):
    game = GameSerializer()

    class Meta:
        model = OrderItem
        fields = (
            "price",
            "game",
            "quantity",
        )

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "price",
            "game",
            "quantity",
        )

class MyOrderSerializer(serializers.ModelSerializer):
    items = MyOrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ( # all fields from the frontend
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "postcode",
            "place",
            "phone",
            "stripe_token",
            "items",
            "paid_amount"
        )

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "postcode",
            "place",
            "phone",
            "stripe_token",
            "items",
        )

    def create(self, validated_data): # overriding create function
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data) # creates new order based on the validated form

        for item_data in items_data: # loops through all items in the list
            OrderItem.objects.create(order=order, **item_data) # create new item
        
        return order