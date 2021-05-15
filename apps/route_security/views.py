from django.shortcuts import render
from apps.accounts.permission import IsAdminUser, IsLoggedInUserOrSuperAdmin, IsAdminOrAnonymousUser
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.

class RoutingsecStatViewSet(viewsets.ReadOnlyModelViewSet):
    # Lister les Asn et afficher le nombre total d'asn
        queryset = models.RoutingsecStat.objects.all()
        serializer_class = serializers.RoutingsecStatSerializer
        filter_backends = [filters.DjangoFilterBackend,]
        filterset_fields = ['save_at']

