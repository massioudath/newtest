from rest_framework import serializers
from . import models
class RepartitionTechnologieSerializer(serializers.ModelSerializer):
    class Meta:
        #year = serializers.DateField(format='%Y')
        model = models.RepartitionTechnologie
        fields = ('technologie', 'repartition', 'year', 'created_at')

    def create(self, validated_data):
        repartition = models.RepartitionTechnologie(
            technologie=validated_data['technologie'],
            repartition=validated_data['repartition'],
            year=validated_data['year'],
        )   

        repartition.save()
        return repartition

    def update(self, instance,validated_data):
        
        instance.technologie = validated_data['technologie'],
        instance.repartition = validated_data['repartition'],
        instance.year = validated_data['year'],

        instance.save()
        return instance