from django.db import models
from account.models import Profile


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='itcat')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='itprof')

    def __str__(self):
        return self.name


class Order(models.Model):
    quantity = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='oritem')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='orprof')

    def __str__(self):
        return self.quantity




