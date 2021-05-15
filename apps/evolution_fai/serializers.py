from rest_framework import serializers
from . import models
#Serelisation Domain
class EvolutionFaiSerializer(serializers.ModelSerializer):
    class Meta:
        #year = serializers.DateField(format='%Y')
        model = models.EvolutionFai
        fields = ('operateur', 'evolution', 'year', 'created_at')

    def create(self, validated_data):
        evolution = models.EvolutionFai(
            technologies=validated_data['technologies'],
            evolution=validated_data['evolution'],
            year=validated_data['year'],
        )   

        evolution.save()
        return evolution

    def update(self, instance,validated_data):
        
        instance.technologies = validated_data['technologies'],
        instance.evolution = validated_data['evolution'],
        instance.year = validated_data['year'],

        instance.save()
        return instance
    

