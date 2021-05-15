from rest_framework import serializers
from . import models
#Serelisation ipasn
class RoutingsecStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RoutingsecStat
        fields = ('id', 'nbre_prefixeip_tested','nbre_ro_true', 'nbre_rpki_true',  'save_at')
