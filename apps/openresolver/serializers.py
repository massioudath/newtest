from rest_framework import serializers
from . import models
#Serelisation ipasn
class Opendnsv4StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Opendnsv4Stat
        fields = ('id', 'nbre_odr', 'save_at')
