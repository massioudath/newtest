# Create your views here.

from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from django.http import Http404
from rest_framework.permissions import AllowAny
from apps.accounts.permission import IsAdminUser, IsLoggedInUserOrSuperAdmin, IsAdminOrAnonymousUser
from django_filters import rest_framework as filters
from django.db.models import Max
from django.db.models import FloatField
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


# Create your views here.

class CoutFibreOptiqueViewSet(viewsets.ModelViewSet):
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
    queryset = models.CoutFibreOptique.objects.all()
    serializer_class = serializers.CoutFibreOptiqueSerializer
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_fields = ['year','created_at',]

class CoutAdslViewSet(viewsets.ModelViewSet):
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
    queryset = models.CoutAdsl.objects.all()
    serializer_class = serializers.CoutAdslSerializer
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_fields = ['year','created_at',]

class CoutGoInternetMobileViewSet(viewsets.ModelViewSet):
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
    queryset = models.CoutGoInternetMobile.objects.all()
    serializer_class = serializers.CoutGoInternetMobileSerializer
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_fields = ['operateur','year','created_at',]
     
class CoutGoInternetMobileView(APIView):
    """
    A view that returns the count of active users in JSON.
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None): 
        value = models.CoutGoInternetMobile.objects.all().aggregate(Max('cout', output_field=FloatField()))
        content = {'value': value}
        return Response(content)     

class LicenceFaiViewSet(viewsets.ModelViewSet):
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
    queryset = models.LicenceFai.objects.all()
    serializer_class = serializers.LicenceFaiSerializer
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_fields = ['year','created_at',]

class LicenceGsmViewSet(viewsets.ModelViewSet):
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
    queryset = models.LicenceGsm.objects.all()
    serializer_class = serializers.LicenceGsmSerializer
    filter_backends = [filters.DjangoFilterBackend,]
    filterset_fields = ['year','created_at',]
