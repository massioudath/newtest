from rest_framework import serializers
from . import models
#Serelisation Domain
class PenetrationSerializer(serializers.ModelSerializer):
    class Meta:
        #year = serializers.DateField(format='%Y')
        model = models.Penetration
        fields = ('id', 'internet_fixe', 'internet_mobile', 'year', 'created_at')

    def create(self, validated_data):
        penetration = models.Penetration(
            internet_fixe=validated_data['internet_fixe'],
            internet_mobile=validated_data['internet_mobile'],
            year=validated_data['year'],
        )   

        penetration.save()
        return penetration

    def update(self, instance,validated_data):
        
        instance.internet_fixe = validated_data[' internet_fixe'],
        internet_mobile=validated_data['internet_mobile'],
        instance.year = validated_data['year'],

        instance.save()
        return instance

