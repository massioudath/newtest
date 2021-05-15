from django.db import models

# Create your models here.
#parc abonnes fixe
class ParcAbonnesFixe(models.Model):
    operateur = models.CharField(max_length=255, blank=True, null=True)
    technologie = models.CharField(max_length=255, blank=True, null=True)
    abonnes = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parc_abonnes_fixe'


class ParcAbonnesMobile(models.Model):
    operateur = models.CharField(max_length=255, blank=True, null=True)
    technologie = models.CharField(max_length=255, blank=True, null=True)
    abonnes = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parc_abonnes_mobile'
