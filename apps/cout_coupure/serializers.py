from rest_framework import serializers
from . import models
#Serelisation Domain
class CoutCoupureSerializer(serializers.ModelSerializer):
    class Meta:
        #year = serializers.DateField(format='%Y')
        model = models.CoutCoupure
        fields = ('id','cout_coupure_internet','cout_coupure_facebook','cout_coupure_twitter','cout_coupure_instagram','cout_coupure_whatsapp','created_at')
    
    def create(self, validated_data):
            val = models.CoutCoupure(
            cout_coupure_internet=validated_data['cout_coupure_internet'],
            cout_coupure_facebook=validated_data['cout_coupure_facebook'],
            cout_coupure_twitter=validated_data['cout_coupure_twitter'],
            cout_coupure_instagram=validated_data['cout_coupure_instagram'],
            cout_coupure_whatsapp=validated_data['cout_coupure_whatsapp'],
        )   
            val.save()
            return val

    def update(self, instance,validated_data):
        instance.cout_coupure_internet=validated_data['cout_coupure_internet'],
        instance.cout_coupure_facebook=validated_data['cout_coupure_facebook'],
        instance.cout_coupure_twitter=validated_data['cout_coupure_twitter'],
        instance.cout_coupure_instagram=validated_data['cout_coupure_instagram'],
        instance.cout_coupure_whatsapp=validated_data['cout_coupure_whatsapp'],
        instance.save()
        return instance