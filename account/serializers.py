from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from . import models


class ProfileSerializerSender(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20, validators=[UniqueValidator(queryset=models.User.objects.all())],
                                     write_only=True)
    password = serializers.CharField(max_length=20, write_only=True)
    password2 = serializers.CharField(max_length=20, write_only=True)

    def create(self, validated_data):
        user = models.User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        profile = models.Profile.objects.create(
            is_sender=True,
            user=user
        )
        return profile

    class Meta:
        model = models.Profile
        exclude = ['user', 'is_sender']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Пароли не совподают!')
        return data


class ProfileSerializerBuyer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20, validators=[UniqueValidator(queryset=models.User.objects.all())],
                                     write_only=True)
    password = serializers.CharField(max_length=20, write_only=True)
    password2 = serializers.CharField(max_length=20, write_only=True)

    def create(self, validated_data):
        user = models.User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        profile = models.Profile.objects.create(
            is_sender=False,
            user=user
        )
        return profile

    class Meta:
        model = models.Profile
        exclude = ['user', 'is_sender']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Пароли не совподают!')
        return data