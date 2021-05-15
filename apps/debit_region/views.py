# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from apps.accounts.permission import IsAdminUser, IsLoggedInUserOrSuperAdmin, IsAdminOrAnonymousUser
from django_filters import rest_framework as filters

# Create your views here.

class DebitRegionViewSet(viewsets.ReadOnlyModelViewSet):
    # Lister les Asn et afficher le nombre total d'asn
        queryset = models.DebitRegion.objects.all()
        serializer_class = serializers.DebitRegionSerializer
        filter_backends = [filters.DjangoFilterBackend,]
        filterset_fields = ['region','created_at']
