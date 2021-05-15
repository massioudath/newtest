from rest_framework import serializers
from . import models
#Serelisation Domain
class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Domain
        fields = ('id', 'total_domain', 'actifs_domain', 'expired_domain', 'year', 'created_at')

    def create(self, validated_data):
        domain = models.Domain(
            total_domain=validated_data['total_domain'],
            actifs_domain=validated_data['actifs_domain'],
            expired_domain=validated_data['expired_domain'],
            year=validated_data['year'],
        )   

        domain.save()
        return domain

    def update(self, instance,validated_data):
        
        instance.total_domain = validated_data[' total_domain'],
        instance.actifs_domain = validated_data['actifs_domain'],
        instance.expired_domain = validated_data['expired_domain'],
        instance.year = validated_data['year']
       

        instance.save()
        return instance
