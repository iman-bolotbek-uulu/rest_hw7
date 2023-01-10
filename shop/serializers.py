from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    # profile = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Item
        # fields = ('name', 'price', 'category', 'profile')
        exclude = ['profile', ]
        # read_only_fields = ['profile', ]


class OrderSerializer(serializers.ModelSerializer):
    # profile = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Order
        exclude = ['profile', ]
        # fields = '__all__'
    #     read_only_fields = ['profile', ]

