from django.db import models

# Create your models here.

class CoutFibreOptique(models.Model):
    cout = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'cout_fibre_optique'

class CoutAdsl(models.Model):
    cout = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'cout_adsl'
    
class CoutGoInternetMobile(models.Model):
    operateur = models.CharField(max_length=50, blank=True, null=True)
    cout = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'cout_go_internet_mobile'

class LicenceFai(models.Model):
    cout = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'licence_fai'
    
class LicenceGsm(models.Model):
    cout = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'licence_gsm'

