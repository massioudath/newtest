from rest_framework import serializers
from . import models
#Serelisation Domain
class TopSiteSerializer(serializers.ModelSerializer):
    class Meta:
        #year = serializers.DateField(format='%Y')
        model = models.TopSite
        fields = ('id','name','url','created_at')
    def create(self, validated_data):
            top = models.TopSite(
                name=validated_data['name'],
                url=validated_data['url'],
            year=validated_data['year'],
        )   
            top.save()
            return top

    def update(self, instance,validated_data):
        
        instance.name = validated_data['name'],
        instance.url = validated_data['url'],
        instance.save()
        return instance