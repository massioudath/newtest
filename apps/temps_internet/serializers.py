from rest_framework import serializers
from . import models
#Serelisation Domain
class TempsInternetSerializer(serializers.ModelSerializer):
    class Meta:
        #year = serializers.DateField(format='%Y')
        model = models.TempsInternet
        fields = ('id','temps_moyens_internet','created_at')
    def create(self, validated_data):
            temps = models.TempsInternet(
            temps_moyens_internet=validated_data['temps_moyens_internet'],
            )   
            temps.save()
            return temps

    def update(self, instance,validated_data):
        
        instance.temps_moyens_internet = validated_data['temps_moyens_internet'],
        instance.save()
        return instance