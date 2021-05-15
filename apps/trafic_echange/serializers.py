from rest_framework import serializers
from . import models
#Serelisation Domain
class TraficEchangeSerializer(serializers.ModelSerializer):
    class Meta:
        #year = serializers.DateField(format='%Y')
        model = models.TraficEchange
        fields = ('url_trafic','created_at')
    def create(self, validated_data):
            trafic = models.TraficEchange(
            url_trafic=validated_data['url_trafic'],
        )   
            trafic.save()
            return trafic

    def update(self, instance,validated_data):
        
        instance.url_trafic = validated_data['url_trafic'],
        instance.save()
        return instance