from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.permissions import AllowAny
from apps.accounts.permission import IsAdminUser, IsLoggedInUserOrSuperAdmin, IsAdminOrAnonymousUser
from django_filters import rest_framework as filters

# Create your views here.

class RepartitionTechnologieViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminOrAnonymousUser]
        elif self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminOrAnonymousUser]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    serializer_class = serializers.RepartitionTechnologieSerializer
    queryset = models.RepartitionTechnologie.objects.all()
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_fields = ['year','created_at',]
    