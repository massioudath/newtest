from rest_framework import serializers
from . import models
#Serelisation Domain
class RepartitionInternetFixeDebitSerializer(serializers.ModelSerializer):
    class Meta:
        #year = serializers.DateField(format='%Y')
        model = models.RepartitionInternetFixeDebit
        fields = ('debit', 'repartition', 'year', 'created_at')

    def create(self, validated_data):
        repartition = models.RepartitionInternetFixeDebit(
            debit=validated_data['debit'],
            repartition=validated_data['repartition'],
            year=validated_data['year'],
        )   

        repartition.save()
        return repartition

    def update(self, instance,validated_data):
        
        instance.debit = validated_data['debit'],
        instance.repartition = validated_data['repartition'],
        instance.year = validated_data['year'],

        instance.save()
        return instance
    

