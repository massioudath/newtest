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

class IpasnViewSet(viewsets.ReadOnlyModelViewSet):
    # Lister les Asn et afficher le nombre total d'asn
        queryset = models.Ipasn.objects.all()
        serializer_class = serializers.IpasnSerializer
        filter_backends = [filters.DjangoFilterBackend,]
        filterset_fields = ['ipaddr', 'ip_date', 'ip_status', 'asn_num', 'asn_date', 'asn_status', 'owner', 'created_at']

class IpasnAsnViewSet(viewsets.ReadOnlyModelViewSet):
    # Lister les Asn et afficher le nombre total d'asn
        queryset = models.IpasnAsn.objects.all()
        serializer_class = serializers.IpasnAsnSerializer
        filter_backends = [filters.DjangoFilterBackend,]
        filterset_fields = ['created_at']

class IpasnIpv4ViewSet(viewsets.ReadOnlyModelViewSet):
    # Lister les Asn et afficher le nombre total d'asn
        queryset = models.IpasnIpv4.objects.all()
        serializer_class = serializers.IpasnIpv4Serializer
        filter_backends = [filters.DjangoFilterBackend,]
        filterset_fields = ['created_at']

class IpasnIpv6ViewSet(viewsets.ReadOnlyModelViewSet):
    # Lister les Asn et afficher le nombre total d'asn
        queryset = models.IpasnIpv6.objects.all()
        serializer_class = serializers.IpasnIpv6Serializer
        filter_backends = [filters.DjangoFilterBackend,]
        filterset_fields = ['created_at']

