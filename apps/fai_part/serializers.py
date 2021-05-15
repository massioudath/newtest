from rest_framework import serializers
from . import models
#Serelisation Domain
class FaiPartSerializer(serializers.ModelSerializer):
    class Meta:
        #year = serializers.DateField(format='%Y')
        model = models.FaiPart
        fields = ('fai','part','year','created_at')
    def create(self, validated_data):
            value = models.FaiPart(
            fai=validated_data['fai'],
            part=validated_data['part'],
            year=validated_data['year'],
        )   
            value.save()
            return value

    def update(self, instance,validated_data):
        
        instance.fai = validated_data['fai'],
        instance.year = validated_data['year'],
        instance.part = validated_data['part'],
        instance.save()
        return instance