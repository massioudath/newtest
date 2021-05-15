from rest_framework import serializers
from . import models
#Serelisation Domain
class ParcAbonnesFixeSerializer(serializers.ModelSerializer):
    class Meta:
        #annee = serializers.DateField(format='%Y')
        model = models.ParcAbonnesFixe
        fields = ('id', 'technologie', 'operateur', 'abonnes', 'year','created_at')

    def create(self, validated_data):
        
        abonnes = models.ParcAbonnesFixe(
            technologie =validated_data['technologie'],
            operateur=validated_data['operateur'],
            abonnes=validated_data['abonnes'],
            year=validated_data['year'],
        )  
        abonnes.save()
        return abonnes

    def update(self, instance,validated_data):
        instance.technologie = validated_data['technologie'],
        instance.operateur = validated_data['operateur'],
        instance.abonnes = validated_data['abonnes'],
        instance.annee = validated_data['annee'],
       

        instance.save()
        return instance
    
    
class ParcAbonnesMobileSerializer(serializers.ModelSerializer):
    class Meta:
        #annee = serializers.DateField(format='%Y')
        model = models.ParcAbonnesMobile
        fields = ('id', 'technologie', 'operateur', 'abonnes', 'year','created_at')

    def create(self, validated_data):
        
        abonnes = models.ParcAbonnesMobile(
            technologie=validated_data['technologie'],
            operateur=validated_data['operateur'],
            abonnes=validated_data['abonnes'],
            year=validated_data['year'],
        )  
        

        abonnes.save()
        return abonnes

    def update(self, instance,validated_data):
        instance.technologie = validated_data['technologie'],
        instance.operateur = validated_data['operateur'],
        instance.abonnes = validated_data['abonnes'],
        instance.annee = validated_data['annee'],
       

        instance.save()
        return instance
