from rest_framework import serializers
from . import models
#Serelisation Domain
class OperateurMobilePartSerializer(serializers.ModelSerializer):
    class Meta:
        #year = serializers.DateField(format='%Y')
        model = models.OperateurMobilePart
        fields = ('operateur','part','year','created_at')
    def create(self, validated_data):
            value = models.OpearateurMobilePart(
                operateur=validated_data['operateur'],
                part=validated_data['part'],
                year=validated_data['year'],
        )   
            value.save()
            return value

    def update(self, instance,validated_data):
        instance.operateur = validated_data['operateur'],
        instance.part = validated_data['part'],
        instance.year = validated_data['year'],
        instance.save()
        return instance