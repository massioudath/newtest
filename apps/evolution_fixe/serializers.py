from rest_framework import serializers
from . import models

class EvolutionFixeSerializer(serializers.ModelSerializer):
    class Meta:
        #year = serializers.DateField(format='%Y')
        model = models.EvolutionFixe
        fields = ('technologie', 'evolution', 'year', 'created_at')

    def create(self, validated_data):
        evolution = models.EvolutionFixe(
            operateur=validated_data['operateur'],
            evolution=validated_data['evolution'],
            year=validated_data['year'],
        )   

        evolution.save()
        return evolution

    def update(self, instance,validated_data):
        
        instance.operateur = validated_data['operateur'],
        instance.evolution = validated_data['evolution'],
        instance.year = validated_data['year'],

        instance.save()
        return instance