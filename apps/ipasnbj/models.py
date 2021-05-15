# Create your models here.

from django.db import models

# Create your models here.
class Ipasn(models.Model):
    ipaddr = models.CharField(max_length=25, blank=True, null=True)
    cidr = models.CharField(max_length=25, blank=True, null=True)
    ip_date = models.CharField(max_length=25, blank=True, null=True)
    ip_status = models.CharField(max_length=25, blank=True, null=True)
    asn_num = models.CharField(max_length=25, blank=True, null=True)
    asn_date = models.CharField(max_length=25, blank=True, null=True)
    asn_status = models.CharField(max_length=25, blank=True, null=True)
    owner = models.CharField(max_length=225, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ipasn'

class IpasnAsn(models.Model):
    asn = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ipasn_asn'


class IpasnIpv4(models.Model):
    total_ipv4 = models.IntegerField(blank=True, null=True)
    total_ipv4_blacklist = models.IntegerField(blank=True, null=True)
    bloc_ipv4 = models.IntegerField(blank=True, null=True)
    allocated = models.IntegerField(blank=True, null=True)
    assigned = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ipasn_ipv4'


class IpasnIpv6(models.Model):
    total_ipv6 = models.IntegerField(blank=True, null=True)
    total_ipv6_blacklist = models.IntegerField(blank=True, null=True)
    bloc_ipv6 = models.IntegerField(blank=True, null=True)
    allocated = models.IntegerField(blank=True, null=True)
    assigned = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ipasn_ipv6'


