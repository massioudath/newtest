from rest_framework import serializers
from . import models
#Serelisation Domain
class SondeSerializer(serializers.ModelSerializer):
    class Meta:
        #year = serializers.DateField(format='%Y')
        model = models.Sonde
        fields = ('total', 'abandonned','connected', 'disconnected', 'never_connected', 'created_at')