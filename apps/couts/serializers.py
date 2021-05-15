from rest_framework import serializers
from . import models
#Serelisation Domain
class CoutFibreOptiqueSerializer(serializers.ModelSerializer):
    class Meta:
        #year = serializers.DateField(format='%Y')
        model = models.CoutFibreOptique
        fields = ('id','cout','year','created_at')
    def create(self, validated_data):
            val = models.CoutFibreOptique(
            cout=validated_data['cout'],
            year=validated_data['year'],
        )   
            val.save()
            return val

    def update(self, instance,validated_data):
        
        instance.cout = validated_data['cout'],
        instance.year = validated_data['year'],
        instance.save()
        return instance

class CoutAdslSerializer(serializers.ModelSerializer):
    class Meta:
        #year = serializers.DateField(format='%Y')
        model = models.CoutAdsl
        fields = ('id','cout','year','created_at')
    def create(self, validated_data):
            val = models.CoutAdsl(
            cout=validated_data['cout'],
            year=validated_data['year'],
        )   
            val.save()
            return val

    def update(self, instance,validated_data):
        
        instance.cout = validated_data['cout'],
        instance.year = validated_data['year'],
        instance.save()
        return instance
    
class CoutGoInternetMobileSerializer(serializers.ModelSerializer):
    class Meta:
        #year = serializers.DateField(format='%Y')
        model = models.CoutGoInternetMobile
        fields = ('id','operateur','cout','year','created_at')
    def create(self, validated_data):
            val = models.CoutGoInternetMobile(
                operateur=validated_data['operateur'],
                cout=validated_data['cout'],
                year=validated_data['year'],
        )   
            val.save()
            return val

    def update(self, instance,validated_data):
        instance.operateur = validated_data['operateur'],
        instance.cout = validated_data['cout'],
        instance.year = validated_data['year'],
        instance.save()
        return instance
    
class LicenceFaiSerializer(serializers.ModelSerializer):
    class Meta:
        #year = serializers.DateField(format='%Y')
        model = models.LicenceFai
        fields = ('id','cout','year','created_at')
    def create(self, validated_data):
            val = models.LicenceFai(
            cout=validated_data['cout'],
            year=validated_data['year'],
        )   
            val.save()
            return val

    def update(self, instance,validated_data):
        
        instance.cout = validated_data['cout'],
        instance.year = validated_data['year'],
        instance.save()
        return instance
    
class LicenceGsmSerializer(serializers.ModelSerializer):
    class Meta:
        #year = serializers.DateField(format='%Y')
        model = models.LicenceGsm
        fields = ('id','cout','year','created_at')
    def create(self, validated_data):
            val = models.LicenceGsm(
            cout=validated_data['cout'],
            year=validated_data['year'],
        )   
            val.save()
            return val

    def update(self, instance,validated_data):
        
        instance.cout = validated_data['cout'],
        instance.year = validated_data['year'],
        instance.save()
        return instance
    
