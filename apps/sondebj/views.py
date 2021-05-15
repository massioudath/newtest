from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from django_filters import rest_framework as filters
from rest_framework.permissions import AllowAny
from apps.accounts.permission import IsAdminUser, IsLoggedInUserOrSuperAdmin, IsAdminOrAnonymousUser

# Create your views here.
 
class SondeViewSet(viewsets.ReadOnlyModelViewSet):
    
    serializer_class = serializers.SondeSerializer
    queryset = models.Sonde.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['created_at',]
