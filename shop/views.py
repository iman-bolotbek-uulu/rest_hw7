from rest_framework import viewsets
from .permissions import IsSenderPermission
from . import models
from . import serializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [IsSenderPermission, ]


class ItemViewSet(viewsets.ModelViewSet):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer
    permission_classes = [IsSenderPermission, ]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsSenderPermission, ]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)



