from rest_framework import serializers
from . import models
#Serelisation ipasn
class IpasnSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ipasn
        fields = ('id','ipaddr','cidr', 'ip_date', 'ip_status', 'asn_num', 'asn_date', 'asn_status', 'owner', 'created_at')

class IpasnAsnSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IpasnAsn
        fields = ('id','asn','created_at')
        
class IpasnIpv4Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.IpasnIpv4
        fields = ('id','total_ipv4', 'total_ipv6_blacklist', 'bloc_ipv4', 'allocated', 'assigned', 'created_at')

class IpasnIpv6Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.IpasnIpv6
        fields = ('id','total_ipv6', 'total_ipv6_blacklist', 'bloc_ipv6', 'allocated', 'assigned', 'created_at')

