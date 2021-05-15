from rest_framework import serializers
from . import models
#Serelisation Domain
    
class NumberUserSerializer(serializers.ModelSerializer):

    class Meta:
        #year = serializers.DateField(format='%Y')
        model = models.NumberUser
        fields = ('id','abonnes','reseaux','created_at')
        
    def create(self, validated_data):
        val = models.NumberUser(
            reseaux=validated_data['reseaux'],
            abonnes=validated_data['abonnes'],
        )   
        val.save()
        return val

    def update(self, instance,validated_data):
        
        instance.reseaux = validated_data['reseaux'],
        instance.abonnes = validated_data['abonnes'],
        instance.save()
        return instance
    
class ReseauSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReseauSocial
        #year = serializers.DateField(format='%Y')
        fields = ('id','name','created_at')
    def create(self, validated_data):
        val = models.ReseauSocial(
            name=validated_data['name'],
        )   
        val.save()
        return val

    def update(self, instance,validated_data):
        
        instance.name = validated_data['name'],
        instance.save()
        return instance