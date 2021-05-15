from rest_framework import serializers
from . import models

class InternetUsersSerializer(serializers.ModelSerializer):
    class Meta:
        #year = serializers.DateField(format='%Y')
        model = models.InternetUsers
        fields = ('id', 'nbre_users', 'year', 'created_at')

    def create(self, validated_data):
        val = models.InternetUsers(
            nbre_users=validated_data['nbre_users'],
            year=validated_data['year'],
        )   

        val.save()
        return val

    def update(self, instance,validated_data):
        
        instance.nbre_users = validated_data['nbre_users'],
        instance.year = validated_data['year'],

        instance.save()
        return instance