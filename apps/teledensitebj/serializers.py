from rest_framework import serializers
from . import models
#Serelisation Domain
class TeledensiteSerializer(serializers.ModelSerializer):
    class Meta:
        #year = serializers.DateField(format='%Y')
        model = models.Teledensite
        fields = ('teledensite','year','created_at')
    def create(self, validated_data):
            teledensite = models.Teledensite(
            teledensite=validated_data['teledensite'],
            year=validated_data['year'],
        )   
            teledensite.save()
            return teledensite

    def update(self, instance,validated_data):
        
        instance.teledensite = validated_data['teledensite'],
        instance.year = validated_data['year'],
        instance.save()
        return instance