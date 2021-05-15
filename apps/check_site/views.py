from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.permissions import AllowAny
from apps.accounts.permission import IsAdminUser, IsLoggedInUserOrSuperAdmin, IsAdminOrAnonymousUser
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .script import Checkdnssec,CheckTls,CheckNs,CheckMX,CheckIpv6,CheckNsIpv6
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
# Create your views here.

class CheckView(APIView):
    """
    A view that returns the count of active users in JSON.
    """
    renderer_classes = [JSONRenderer] 
    def get(self, request, format=None):
            query = request.GET.get('query')
            if not query:
                response = 'Aucun domaine entrée'
            else:
                response = 'resultat'
                dnssec = Checkdnssec(query)
                tls = CheckTls(query)
                ns = CheckNs(query)
                mx = CheckMX(query)
                ipv6 = CheckIpv6(query)
                nsipv6 = CheckNsIpv6(query)

            context = {
                'response': response,
                'dnssec': dnssec,
                'tls': tls,
                'ns': ns,
                'mx': mx,
                'ipv6': ipv6,
                'nsipv6': nsipv6,
            }
            return Response(context)
