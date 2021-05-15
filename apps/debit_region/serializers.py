from rest_framework import serializers
from . import models

class DebitRegionSerializer(serializers.ModelSerializer):
    class Meta:
        #year = serializers.DateField(format='%Y')
        model = models.DebitRegion
        fields = ('region', 'median_download', 'median_upload','download','upload','created_at')